from copy import deepcopy
from typing import List
from vocabulary import Vocabulary
import _thread


class MultiThreadForward(object):
    def __init__(self, vocabulary: Vocabulary, thread: int = 4):
        self.__vocabulary = deepcopy(vocabulary)
        self.__thread = thread

    def __call__(self, lines: List[List[str]]) -> List[List[str]]:
        length = len(lines) // self.__thread
        position = 0
        for i in range(1, self.__thread):
            _thread.start_new_thread(self.__split,
                                     (lines, position, position + length))
            position += length
        _thread.start_new_thread(self.__split, (lines, position, None))

    def __split(self, lines: List[List[str]], begin: int,
                end: int) -> List[List[str]]:
        for i in range(begin, end):
            lines[i] = self.__forward(lines[i][0])

    def __forward(self, line: str) -> List[str]:
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
