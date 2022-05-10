import qcnlp as qc

text = "一命呜呼，然后上了西天"
# 正向最长匹配分词
f_list = qc.f_seg(text)
print(f_list)
# 逆向最长匹配分词
b_list = qc.b_seg(text)
print(b_list)
# 双向最长匹配分词 + 去除停用词
l_list = qc.l_seg(text)
l_list = qc.remove_stopwords(l_list)
print(l_list)