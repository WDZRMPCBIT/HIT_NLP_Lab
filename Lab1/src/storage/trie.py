from copy import deepcopy
from phrase import Phrase


class Trie:
    def __init__(self):
        self.__root = {}

    def add(self, phrase: Phrase):
        """
        向Trie中添加一个词组

        :param phrase: 待添加的词组
        """
        node = self.__root
        word = phrase.phrase(sep=' ')

        for s in word:
            if s in node.keys():
                node = node[s]
            else:
                node[s] = {}
                node = node[s]
        node['is_word'] = phrase

    def get(self, phrase: str) -> Phrase:
        """
        查询Trie中某个词组是否存在，若不存在，返回None；否则，返回相应的Phrase

        :param phrase: 待查询词组
        """
        node = self.__root

        for s in phrase:
            if s in node.keys():
                node = node[s]
            else:
                return None

        if 'is_word' in node.keys():
            return deepcopy(node['is_word'])
        else:
            return None
