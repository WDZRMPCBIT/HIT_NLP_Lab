from copy import deepcopy
from typing import List
from vocabulary import Vocabulary


class backward(object):
    def __init__(self, vocabulary: Vocabulary):
        self.__vocabulary = deepcopy(vocabulary)

    def __call__(self, line: str) -> List[str]:
        ret: List[str] = []
        length = len(line)
        current = length
        max_length = self.__vocabulary.max_length()

        while current > 0:
            for i in reversed(range(1, min(max_length, current + 1))):
                phrase = self.__vocabulary.get(line[current - i:current])
                if phrase is not None:
                    ret = ret + phrase
                    current = current - i
                    break
                if i == 1:
                    ret = ret + [line[current - 1:current]]
                    current = current - 1

        return reversed(ret)
