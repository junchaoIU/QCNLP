#导入需要的包
import pandas as pd
import csv
import jieba
from pprint import pprint
import gensim

import qcnlp
from qcnlp import stopwords_loader

sentence = pd.read_csv("test.txt",header=None,quoting = csv.QUOTE_NONE,delimiter="\n") #读取文件，记住取名不要用中文
data = sentence[0].tolist() #转换为列表格式

data = qcnlp.remove_stopwords(data)
stop_words = stopwords_loader()
print(data)
# stopwords = pd.read_csv("stop_words_ch.txt",header=None,quoting = csv.QUOTE_NONE,delimiter="\t")
# stopwords = stopwords[0].tolist()
# stopwords.append("时")  #后面发现还有这几个漏网之鱼，继续加到停用词里去
# stopwords.append("一种")
# stopwords.append("请")
# stopwords.append("●")
#
data_cut = [ " ".join(qcnlp.b_seg(line)) for line in data]
print(data_cut)
data_no_stopwords = [[word for word in line.split() if word not in stop_words] for line in data_cut]

from collections import defaultdict
frequency =defaultdict(int)
for line in data_no_stopwords:
    for token in line:
        frequency[token] +=1
data_morethan3times= [[token for token in line if frequency[token]>3]for line in data_no_stopwords]

#训练模型
model =gensim.models.Word2Vec(data_morethan3times,min_count=2,window=5)
#min_count是最低出现数，默认数值是5；
#size是gensim Word2Vec将词汇映射到的N维空间的维度数量（N）默认的size数是100；
#iter是模型训练时在整个训练语料库上的迭代次数，假如参与训练的文本量较少，就需要把这个参数调大一些。iter的默认值为5；
#sg是模型训练所采用的的算法类型：1 代表 skip-gram，0代表 CBOW，sg的默认值为0；
#window控制窗口，如果设得较小，那么模型学习到的是词汇间的组合性关系（词性相异）；如果设置得较大，会学习到词汇之间的聚合性关系（词性相同）。模型默认的window数值为5；

#重要常用方法
print(model.wv.key_to_index) #1.获得所有词汇组