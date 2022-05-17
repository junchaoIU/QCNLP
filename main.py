import qcnlp as qc
print(qc.__version__)

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

text = "QCNLP，是一个小巧的NLP工具吧？是吧。"
c_list = qc.sentence_seg(text,'coarse')
f_list = qc.sentence_seg(text,'fine')
print(c_list)
print(f_list)

text = "我猜，今天天气不错！"
sentiment_score = qc.sentiment_dic(text)
print(sentiment_score)


text = "我要学好林黛玉和鲁迅文学~"
ner_model = qc.NerSearch({"people":["林黛玉","鲁迅"]})
print(ner_model(text))