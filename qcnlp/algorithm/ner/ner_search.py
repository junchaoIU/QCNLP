# -*- coding=utf-8 -*-
"""
# library: qcnlp
# author: wujunchao
# license: Apache License 2.0
# email: wujunchaoIU@outlook.com
# github: https://github.com/junchaoIU/QCNLP
# description: A Preprocessing & Parsing tool for Chinese Natural Language Processing
"""
from qcnlp.data_structure.TrieTree import TrieTree


class NerSearch(object):
    """ 构建基于 Trie 词典的实体识别，采用前向最大匹配算法进行搜索。"""

    def __init__(self, entity_dicts):
        self.trie_tree_obj = TrieTree()
        for typing, entity_list in entity_dicts.items():
            self.trie_tree_obj.build_trie_tree(entity_list, typing)

    def __call__(self, text):
        """
        标注数据，给定一个文本字符串，标注出所有的数据
        Args:
            text: 给定的文本 str 格式
        Return:
            entity_list: 标注的实体列表数据
        """

        record_list = list()  # 输出最终结果
        i = 0
        text_length = len(text)

        while i < text_length:
            pointer_orig = text[i: self.trie_tree_obj.depth + i]
            pointer = pointer_orig.lower()
            step, typing = self.trie_tree_obj.search(pointer)
            if typing is not None:
                record = {'type': typing,
                          'text': pointer_orig[0: step],
                          'offset': [i, step + i]}
                record_list.append(record)
            i += step

        return record_list
