# -*- coding=utf-8 -*-
"""
# library: qcnlp
# author: wujunchao
# license: Apache License 2.0
# email: wujunchaoIU@outlook.com
# github: https://github.com/junchaoIU/QCNLP
# description: A Preprocessing & Parsing tool for Chinese Natural Language Processing
"""

class TrieTree(object):
    """
    Trie 树的算法封装
    """
    def __init__(self):
        self.dict_trie = dict()
        self.depth = 0

    def add_node(self, word, typing):
        """向 Trie 树添加节点。
        Args:
            word(str): 词典中的词汇
            typing(str): 词汇类型
        Returns: None
        """
        word = word.strip()
        if word not in ['', '\t', ' ', '\r']:
            tree = self.dict_trie
            depth = len(word)
            word = word.lower()  # 将所有的字母全部转换成小写
            for char in word:
                if char in tree:
                    tree = tree[char]
                else:
                    tree[char] = dict()
                    tree = tree[char]
            if depth > self.depth:
                self.depth = depth
            if 'type' in tree and tree['type'] != typing:
                # print('ERROR!!! `{}` belongs to both `{}` and `{}`.'.format(
                #         word, tree['type'], typing))
                pass
            else:
                tree['type'] = typing

    def build_trie_tree(self, dict_list, typing):
        """ 创建 trie 树 """
        for word in dict_list:
            self.add_node(word, typing)

    def search(self, word):
        """ 搜索给定 word 字符串中与词典匹配的 entity，
        返回值 None 代表字符串中没有要找的实体，
        如果返回字符串，则该字符串就是所要找的词汇的类型
        """
        tree = self.dict_trie
        res = None
        step = 0  # step 计数索引位置
        for char in word:
            if char in tree:
                tree = tree[char]
                step += 1
                if 'type' in tree:
                    res = (step, tree['type'])
            else:
                break
        if res:
            return res
        return 1, None