from copy import deepcopy
from typing import List
from vocabulary import Vocabulary
import multiprocessing
from tqdm import tqdm


class MultiProcessForward(object):
    def __init__(self, vocabulary: Vocabulary, thread: int = 4):
        self.__vocabulary = deepcopy(vocabulary)
        self.__thread = thread

    def __call__(self, lines: List[List[str]]) -> List[List[str]]:
        ret = multiprocessing.Manager().list()
        for i in range(len(lines)):
            ret.append([])
        process = []

        length = len(lines) // self.__thread
        position = 0
        for i in range(1, self.__thread):
            process.append(multiprocessing.Process(
                target=self._split,
                args=(lines, position, position + length, ret, )))
            position += length
        process.append(multiprocessing.Process(
            target=self._split, args=(lines, position, len(lines), ret, )))

        for p in process:
            p.start()
        for p in process:
            p.join()

        return list(ret)

    def _split(self, lines: List[List[str]], begin: int,
               end: int, ret: List[List[str]]):
        for i in tqdm(range(begin, end)):
            ret[i] = self._forward(lines[i][0])

    def _forward(self, line: str) -> List[str]:
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
