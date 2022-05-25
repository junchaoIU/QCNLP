#导入需要的包
from pprint import pprint

import pandas as pd
import csv
import gensim
import qcnlp
from tqdm import tqdm
from qcnlp import stopwords_loader

class Word2vecModel():
    def __init__(self):
        self.stopwords_list = stopwords_loader()

    def __call__(self, data_path, min_count = 1, vector_size = 100 ,epochs = 5, sg = 0, window = 5):
        self.data_path = data_path

        sentence = pd.read_csv(self.data_path, header=None, quoting=csv.QUOTE_NONE, delimiter="\n")  # 读取文件，记住取名不要用中文
        data = sentence[0].tolist()  # 转换为列表格式

        stop_words = self.stopwords_list

        data_cut = []
        print("=" * 10 + "begin to spilt the sentence" + "=" * 10)
        for line in tqdm  (data):
            data_cut.append(" ".join(qcnlp.b_seg(line)) )
        # data_cut = [" ".join(qcnlp.b_seg(line)) for line in data]

        print("=" * 10 + "sentence seg finished" + "=" * 10)

        data_no_stopwords = [[word for word in line.split() if word not in stop_words] for line in data_cut]


        # from collections import defaultdict
        # frequency = defaultdict(int)
        # for line in data_no_stopwords:
        #     for token in line:
        #         frequency[token] += 1
        # data_morethan3times = [[token for token in line if frequency[token] > 3] for line in data_no_stopwords]

        # 训练模型
        print("="*10 +"begin to train word2vec model"+"="*10)
        model = gensim.models.Word2Vec(data_no_stopwords, min_count = min_count, vector_size = vector_size, epochs = epochs, sg = sg, window = window)
        print("=" * 10 + "Finished" + "=" * 10)
        return model
        # min_count是最低出现数，默认数值是5；
        # size是gensim Word2Vec将词汇映射到的N维空间的维度数量（N）默认的size数是100；
        # iter是模型训练时在整个训练语料库上的迭代次数，假如参与训练的文本量较少，就需要把这个参数调大一些。iter的默认值为5；
        # sg是模型训练所采用的的算法类型：1 代表 skip-gram，0代表 CBOW，sg的默认值为0；
        # window控制窗口，如果设得较小，那么模型学习到的是词汇间的组合性关系（词性相异）；如果设置得较大，会学习到词汇之间的聚合性关系（词性相同）。模型默认的window数值为5；

        # # 重要常用方法
        # model.wv.key_to_index  # 1.获得所有词汇组
        # model.wv['爱情']  # 2.获得所有词汇组
        # # # 计算两个词之间的余弦相似度
        # model.wv.similarity('爱情', '疯狂')  # 0.16419926
        # model.wv.most_similar("爱情")  # 最相似的词
        # model.most_similar(positive=['女人', '先生'], negative=['男人'], topn=1)  # 类似于女人+先生-男人的结果
        # # 找出不太合群的词
        # model.wv.doesnt_match("疯狂 痛苦 包含".split())  # 这个结果是包含，但是我发现有时候另外一些词并不能正确判断，所以估计还是语料库不够大
        # # 返回与爱情最近的词和相似度
        # model.wv.similar_by_word("爱情", topn=10, restrict_vocab=30)
        # # 其中的参数restrict_vocab ，它是可选的整数，它限制了向量的范围，搜索最相似的值。 例如，restrict_vocab = 10000会，只检查词汇顺序中的前10000个词汇向量。
        # # 查看词向量的维度,109个词汇，维度为100
        # model.wv.vectors.shape
        # # 给定上下文词汇作为输入，可以获得中心词汇的概率分布
        # pprint(model.predict_output_word(['痛苦', '疯狂', '狂热'], topn=10))

        # 训练损失计算(Training Loss Computation)，当训练Word2Vec模型时，将其中的参数compute_loss设置为True，则可计算训练Word2Vec模型时所得到的损失（Training Loss），它可以衡量模型的训练质量。
        # 计算出的损失存储在模型的属性running_trai型本身丢掉，只留下这个词向量的结果

        # model = Word2Vec.load(file_path)
        # # 接下来整理一些自己的语料
        # corpus = [['你好', '我爱', 'python'], ['编程', '很美']]
        # model.build_vocab(corpus, update=True)
        # model.train(corpus, total_examples=model.corpus_count, epochs=model.iter)

        # 加载保存的模型，再训练，不会更新原有的向量表示
        # 保存成orginal C word2vec - tool 的格式，网上很多预训练模型都保存成了这种模式
        # model.wv.save_word2vec_format(file_path)

