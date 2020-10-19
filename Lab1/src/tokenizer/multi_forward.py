from copy import deepcopy
from typing import List
from vocabulary import Vocabulary


class MultiThreadForward(object):
    def __init__(self, vocabulary: Vocabulary, thread: int = 4):
        self.__vocabulary = deepcopy(vocabulary)
        self.__thread = thread

    def __call__(self, line: str) -> List[str]:
        