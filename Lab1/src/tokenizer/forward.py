from copy import deepcopy
from typing import List
from vocabulary import Vocabulary


class forward(object):
    def __init__(self, vocabulary: Vocabulary):
        self.__vocabulary = deepcopy(vocabulary)

    def __call__(self, line: str) -> List[str]:
        ret: List[str] = []
        current = 0
        length = len(line)
        max_length = self.__vocabulary.max_length()

        while current < length:
            for i in reversed(range(1, min(max_length, length - current + 1))):
                phrase = self.__vocabulary.get(line[current:current + i])
                if phrase is not None:
                    ret = ret + phrase
                    current = current + i
                    break
                if i == 1:
                    ret = ret + [line[current:current + 1]]
                    current = current + 1

        return ret
