from typing import List
from copy import deepcopy


def esitmate(predicate: str, standard: str, output: str):
    """
    计算一个分词结果的准确率, 召回率, F1

    :param predicate: 待评估文件路径
    :param standard: 分词标准文件路径
    :param output: 结果输出路径
    :param max_line: 处理最大行数
    """
    standard_sum = 0
    standard_paragraph: List[List[str]] = []
    with open(standard, 'r') as f:
        for line in f:
            words = line.split()
            standard_paragraph.append(deepcopy(words))
            standard_sum += len(words)

    predicate_sum = 0
    match = 0
    with open(predicate, 'r') as f:
        i = 0
        for line in f:
            words = line.split()
            predicate_sum += len(words)
            for w in words:
                if w in standard_paragraph[i]:
                    match += 1
            i += 1

    precision = match / standard_sum
    callback = match / predicate_sum
    F1 = 2 * precision * callback / (precision + callback)

    with open(output, 'w') as f:
        f.write("precision: " + str(precision) + "\n")
        f.write("callback: " + str(callback) + "\n")
        f.write("F1: " + str(F1) + "\n")


if __name__ == "__main__":
    esitmate("../result/forward.txt", "../result/simplified.txt",
             "../result/score.txt")
