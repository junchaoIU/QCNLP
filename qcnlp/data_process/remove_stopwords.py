# -*- coding=utf-8 -*-
"""
# library: qcnlp
# author: wujunchao
# license: Apache License 2.0
# email: wujunchaoIU@outlook.com
# github: https://github.com/junchaoIU/QCNLP
# description: A Preprocessing & Parsing tool for Chinese Natural Language Processing
"""

from qcnlp.dictionary.dictionary_loader import stopwords_loader

class RemoveStopwords(object):
    """
        先验输入text_segs：分词结果
        输出：去除stopwords后的text_segs
    """

    def __init__(self):
        self.stopwords_list = None

    def _prepare(self):
        self.stopwords_list = stopwords_loader()

    def __call__(self, text_segs):

        if self.stopwords_list is None:
            self._prepare()

        new_text_segs = []

        for word in text_segs:
            # rule0: 空字符串过滤
            if word == '':
                continue

            if word in self.stopwords_list:
                continue
            else:
                new_text_segs.append(word)

        return new_text_segs