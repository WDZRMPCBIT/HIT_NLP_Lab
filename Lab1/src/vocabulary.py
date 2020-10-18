from typing import List
from copy import deepcopy


class Vocabulary(object):
    def __init__(self, storage):
        self.__vocabulary: List[Phrase] = []
        self.__storage = deepcopy(storage)

    def add(self, words: List[str], occ: int):
        """
        向词组表中添加一个词组

        :param words: 要添加的词组
        :param occ: 词组出现的次数
        """
        current = Phrase(words, occ)
        if self.__storage.get(current.phrase()) == -1:
            self.__storage.add(current.phrase(), occ)
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

    def load(path: str, length: int, storage):
        """
        从词典文件中加载词组
        词典文件每一行的格式为：
        词组单词个数 词组出现次数 单词1 单词2 ...

        :param path: 词典文件路径
        :param length: 词组单词的最大个数
        :param storage: 词典组织类
        """
        ret = Vocabulary(storage)
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                items = line.split()

                if int(items[0]) > length:
                    break
                ret.add(items[2:], items[1])
        return ret

    def max_length(self):
        """
        返回词典中词组的最大长度
        由于采用了枚举查找最大长度，所以尽量减少该方法的调用
        """
        ret = 0
        for phrase in self.__vocabulary:
            ret = max(ret, phrase.length())
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
        for i in range(len(self.__words)):
            if i != 0:
                ret = ret + " "
            ret = ret + self.__words[i]
        return ret

    def occ(self):
        """
        返回该词组出现的次数
        """
        return self.__occ

    def length(self):
        """
        返回组成词组的字的个数
        """
        return len(self.phrase())
