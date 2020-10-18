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
            for i in reversed(range(max_length)):
                if self.__vocabulary.get([line[current: current+i]]):
                    ret.append(line[current: current+i])
                    current = current + i
                    break

        return ret
