import qcnlp as qcnlp

text = "中国队牛逼！"
seg = qcnlp.segmation.LongestSeg()
list = seg(text)
print(list)