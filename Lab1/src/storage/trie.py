from typing import List
from copy import deepcopy
from phrase import Phrase


class Trie:
    def __init__(self):
        self.__base: List[int] = [0]
        self.__check: List[int] = [0]
        self.__tail = [0]

    def __extend(self):
        self.__base = self.__base + ([0] * len(self.__base))
        self.__check = self.__check + ([0] * len(self.__check))
        self.__tail = self.__tail + ([0] * len(self.__tail))

    def add(self, phrase: Phrase):
        """
        向Trie中添加一个词组

        :param phrase: 待添加的词组
        """
        pass

    def get(self, phrase: str) -> Phrase:
        """
        查询Trie中某个词组是否存在，若不存在，返回None；否则，返回相应的Phrase

        :param phrase: 待查询词组
        """
        pass

    def __encode(self, word) -> int:
        """
        将一个字编码成一个数
        保证不同的字得到的数不相同

        :param word: 待编码的数
        """
        pass
