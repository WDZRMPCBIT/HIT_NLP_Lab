from copy import deepcopy


def check_not_mark(word: str) -> bool:
    if word == "。":
        return False
    if word == "《":
        return False
    if word == "》":
        return False
    if word == "，":
        return False
    if word == "“":
        return False
    if word == "”":
        return False
    if word == "、":
        return False
    if word == "！":
        return False
    if word == "？":
        return False
    if word == "‘":
        return False
    if word == "’":
        return False
    if word == "（":
        return False
    if word == "）":
        return False
    if word == "［":
        return False
    if word == "］":
        return False
    return True


if __name__ == '__main__':
    import os
    os.chdir("../data")

    single_dictionary = []
    double_dictionary = []
    single_cnt = {}
    double_cnt = {}

    with open('199801_seg&pos.txt') as f:
        for line in f:
            words = line.split()

            for i in range(len(words)):
                single_dictionary.append(
                    (words[i].split('/'))[0].strip('[').strip(']'))

                last = len(single_dictionary) - 1
                if i != 0:
                    pre_word = deepcopy(single_dictionary[last - 1])
                    current_word = deepcopy(single_dictionary[last])
                    if check_not_mark(pre_word) and check_not_mark(
                            current_word):
                        double_dictionary.append(pre_word + ' ' + current_word)

    for w in single_dictionary:
        single_cnt[w] = single_cnt.get(w, 0) + 1
    for w in double_dictionary:
        double_cnt[w] = double_cnt.get(w, 0) + 1

    single_dictionary = list(set(single_dictionary))
    single_dictionary = sorted(single_dictionary)
    double_dictionary = list(set(double_dictionary))
    double_dictionary = sorted(double_dictionary)

    os.chdir("../result")
    with open('dic.txt', 'w') as f:
        for w in single_dictionary:
            f.write('1 ' + w + ' ' + str(single_cnt[w]) + '\n')
        for w in double_dictionary:
            f.write('2 ' + w + ' ' + str(double_cnt[w]) + '\n')
