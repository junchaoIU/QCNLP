# -*- coding=utf-8 -*-
"""
# library: qcnlp
# author: wujunchao
# license: Apache License 2.0
# email: wujunchaoIU@outlook.com
# github: https://github.com/junchaoIU/QCNLP
# description: A Preprocessing & Parsing tool for Chinese Natural Language Processing
"""

from .word2vec import Word2vecModel
from .bertvec import BertvecModel

word2vec_model = Word2vecModel()
bertvec_model = BertvecModel()