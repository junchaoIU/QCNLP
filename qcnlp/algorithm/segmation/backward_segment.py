# -*- coding=utf-8 -*-
"""
# library: qcnlp
# author: wujunchao
# license: Apache License 2.0
# email: wujunchaoIU@outlook.com
# github: https://github.com/junchaoIU/QCNLP
# description: A Preprocessing & Parsing tool for Chinese Natural Language Processing
"""

class BackwardSeg(object):
    """
    分词
    """

    def load_dictionary(self):
        dic = set()

        # 按行读取字典文件，每行第一个空格之前的字符串提取出来。
        for line in open("qcnlp/data/CoreNatureDictionary.txt", "r", encoding="utf8"):
            dic.add(line[0:line.find('	')])

        return dic

    def backward_segment(self,text, dic):
        word_list = []
        i = len(text) - 1
        while i >= 0:  # 扫描位置作为终点
            longest_word = text[i]  # 扫描位置的单字
            for j in range(0, i):  # 遍历[0, i]区间作为待查询词语的起点
                word = text[j: i + 1]  # 取出[j, i]区间作为待查询单词
                if word in dic:
                    if len(word) > len(longest_word):  # 越长优先级越高
                        longest_word = word
                        break
            word_list.insert(0, longest_word)  # 逆向扫描，所以越先查出的单词在位置上越靠后
            i -= len(longest_word)
        return word_list

    def __init__(self):
        self.text = None

    def __call__(self, text):
        # 精确模式
        dic = self.load_dictionary()
        # list = jieba.lcut(text, cut_all = False)
        return self.backward_segment(text, dic)

