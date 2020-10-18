from typing import List


class LinearList(object):
    def __init__(self):
        self.__dictionary: List[str] = []

    def add(self, phrase: str, occ: int):
        """
        向线性表中添加一个词组

        :param phrase: 待添加词组
        :param occ: 该词组出现的次数
        """
        self.__dictionary.append(phrase)

    def get(self, phrase: str) -> int:
        """
        查询线性表中某个词组是否存在，若不存在，返回-1；否则，返回任意值

        :param phrase: 待查询词组
        """
        if phrase in self.__dictionary:
            return 1
        return -1
