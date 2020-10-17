from typing import List
from copy import deepcopy


class Vocabulary(object):
    def __init__(self, storage):
        self.__vocabulary: List[Phrase] = []
        self.__storage = deepcopy(storage)

    def add(self, words: List[str], occ: List[int]):
        """
        向词组表中添加一个词组

        :param words: 要添加的词组
        :param occ: 词组出现的次数
        """
        current = Phrase(words, occ)
        if self.__storage.get(current.phrase()) == -1:
            self.__storage.add(current.add(current.phrase()))
            self.__vocabulary.append(current)

    def get(self, words: List[str]) -> bool:
        """
        从词组表中查询一个单词是否存在
        若存在，则返回True

        :param words: 待查询的单词
        """
        current = Phrase(words, 0)
        if self.__storage.get(current.phrase()) != -1:
            return True
        return False

    def load(self, path: str, storage):
        """
        从词典文件中加载词组
        词典文件每一行的格式为：
        词组单词个数 词组出现次数 单词1 单词2 ...

        :param path: 词典文件路径
        :param storage: 词典组织类
        """
        ret = Vocabulary(storage)
        with open(path, 'r') as f:
            for line in f:
                items = line.split()
                ret.add(items[2:], items[1])
        return ret


class Phrase(object):
    def __init__(self, words: List[str], occ: int):
        """
        表示一个词组

        :param words: 词组
        :paran occ: 词组出现的次数，若为临时使用，请设为0
        """
        self.__words = deepcopy(words)
        self.__occ = occ

    def words(self):
        """
        将存储的词组以List[str]的形式返回
        """
        return deepcopy(self.__words)

    def phrase(self):
        """
        将存储的词组以单个string的形式返回
        """
        ret: str = ""
        for i in range(self.length()):
            if i != 0:
                ret = ret + " "
            ret = ret + self.__words[i]
        return ret

    def occ(self):
        return self.__occ

    def length(self):
        return len(self.__words)
