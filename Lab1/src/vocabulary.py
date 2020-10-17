from typing import List
from copy import deepcopy


class Vocabulary(object):
    def __init__(self, storage):
        self.__words: List[str] = []
        self.__storage = deepcopy(storage)

    def add(self, word: str) -> None:
        """
        将给定的单词插入单词表中

        :param word: 待插入的单词
        """
        if word in self.__words is not True:
            self.__words.append(word)
            self.__storage.add(word)

    def get(self, word: str) -> int:
        """
        查询给定词的哈希值，若词典中不存在则返回-1

        :param word: 待查询词
        """
        if word in self.__words:
            return self.__storage.get(word)
        return -1
