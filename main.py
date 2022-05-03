


import qcnlp as qcnlp

text = "中国队牛逼！"
seg = qcnlp.segmation.TextSeg()
list = seg(text)
print(list)