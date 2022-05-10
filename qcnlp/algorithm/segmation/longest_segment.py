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


class LongestSeg(object):
    """
    双向最长匹配分词
    """

    def count_single_char(self, word_list: list):  # 统计单字成词的个数
        return sum(1 for word in word_list if len(word) == 1)

    def load_dictionary(self):
        dic = set()

        # 按行读取字典文件，每行第一个空格之前的字符串提取出来。
        for line in open("qcnlp/data/CoreNatureDictionary.txt", "r", encoding="utf8"):
            dic.add(line[0:line.find('	')])

        return dic

    def longest_segment(self,text):
        fseg = ForwardSeg()
        bseg = BackwardSeg()
        f = fseg(text)
        b = bseg(text)
        if len(f) < len(b):  # 词数更少优先级更高
            return f
        elif len(f) > len(b):
            return b
        else:
            if self.count_single_char(f) < self.count_single_char(b):  # 单字更少优先级更高
                return f
            else:
                return b  # 都相等时逆向匹配优先级更高

    def __init__(self):
        self.text = None

    def __call__(self, text):
        # 双向最长匹配分词
        return self.longest_segment(text)

