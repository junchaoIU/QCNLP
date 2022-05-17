# -*- coding=utf-8 -*-
"""
# library: qcnlp
# author: wujunchao
# license: Apache License 2.0
# email: wujunchaoIU@outlook.com
# github: https://github.com/junchaoIU/QCNLP
# description: A Preprocessing & Parsing tool for Chinese Natural Language Processing
"""

from .segmation.backward_segment import BackwardSeg
from .segmation.forward_segment import ForwardSeg
from .segmation.longest_segment import LongestSeg
from .segmation.sentence_segment import SentenceSeg
from .sentiment.dic_sentiment import DictionarySentiment
from .ner.ner_search import NerSearch


b_seg = BackwardSeg()
f_seg = ForwardSeg()
l_seg = LongestSeg()
sentence_seg = SentenceSeg()
sentiment_dic = DictionarySentiment()