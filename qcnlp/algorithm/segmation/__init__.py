# -*- coding=utf-8 -*-
"""
# library: qcnlp
# author: wujunchao
# license: Apache License 2.0
# email: wujunchaoIU@outlook.com
# github: https://github.com/junchaoIU/QCNLP
# description: A Preprocessing & Parsing tool for Chinese Natural Language Processing
"""

from .backward_segment import BackwardSeg
from .forward_segment import ForwardSeg
from .longest_segment import LongestSeg
from .sentence_segment import SentenceSeg

b_seg = BackwardSeg()
f_seg = ForwardSeg()
l_seg = LongestSeg()
sentence_seg = SentenceSeg()

