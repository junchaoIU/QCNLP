# -*- coding=utf-8 -*-
"""
# library: qcnlp
# author: wujunchao
# license: Apache License 2.0
# email: wujunchaoIU@outlook.com
# github: https://github.com/junchaoIU/QCNLP
# description: A Preprocessing & Parsing tool for Chinese Natural Language Processing
"""

class ForwardSeg(object):
    """
    正向最长匹配分词
    """

    def load_dictionary(self):
        dic = set()

        # 按行读取字典文件，每行第一个空格之前的字符串提取出来。
        for line in open("qcnlp/data/CoreNatureDictionary.txt", "r", encoding="utf8"):
            dic.add(line[0:line.find('	')])

        return dic

    def forward_segment(self,text, dic):
        word_list = []
        i = 0
        while i < len(text):
            longest_word = text[i]  # 当前扫描位置的单字
            for j in range(i + 1, len(text) + 1):  # 所有可能的结尾
                word = text[i:j]  # 从当前位置到结尾的连续字符串
                if word in dic:  # 在词典中
                    if len(word) > len(longest_word):  # 并且更长
                        longest_word = word  # 则更优先输出
            word_list.append(longest_word)  # 输出最长词
            i += len(longest_word)  # 正向扫描
        return word_list

    def __init__(self):
        self.text = None

    def __call__(self, text):
        # 正向最长匹配分词
        dic = self.load_dictionary()
        return self.forward_segment(text, dic)

