# -*- coding=utf-8 -*-
"""
# library: qcnlp
# author: wujunchao
# license: Apache License 2.0
# email: wujunchaoIU@outlook.com
# github: https://github.com/junchaoIU/QCNLP
# description: A Preprocessing & Parsing tool for Chinese Natural Language Processing
"""


import jieba

class TextSeg(object):
    """
    分词
    """

    def __init__(self):
        self.text = None

    def __call__(self, text):
        # 精确模式
        list = jieba.lcut(text, cut_all = False)
        return list

