from typing import List
from copy import deepcopy


class Paragraph(object):
    def __init__(self, lines: List[List[str]]):
        self.__lines = deepcopy(lines)
        self.__tokenized = False

    def set_tokenized(self):
        self.__tokenized = True

    def tokenized(self):
        """
        返回文章是否已经分词
        """
        return self.__tokenized

    def lines(self):
        """
        返回文章的全文
        """
        return deepcopy(self.__lines)

    def length(self):
        """
        返回文章的行数
        """
        return len(self.__lines)

    def tokenize(self, tokenizer):
        """
        根据所给的单词表、分词器对文章进行分词

        :param tokenizer: 分词器
        """
        if self.__tokenized:
            return

        for i in range(self.length()):
            self.__lines[i] = tokenizer(self.__lines[i])
        self.set_tokenized()

    def load(self, path: str, tokenized: bool):
        """
        从数据文件中读取文章

        :param path: 文章路径
        :param tokenized: 读取的文章是否已完成分词
        """
        lines: List[List[str]] = []
        with open(path, 'r') as f:
            for line in f:
                lines.append(line.split())

        paragraph = Paragraph(lines)
        if tokenized:
            paragraph.set_tokenized()
        return Paragraph(paragraph)

    def save(self, path: str):
        """
        将文章保存到指定路径

        :param path: 保存路径
        """
        with open(path, 'w') as f:
            for line in self.__lines():
                for word in line:
                    f.write(word + " ")
                f.write("\n")
