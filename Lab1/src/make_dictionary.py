import os
os.chdir("../data")

dictionary = []

with open('199801_seg&pos.txt') as f:
    for line in f:
        words = line.split()
        for w in words:
            dictionary.append((w.split('/'))[0].strip('[').strip(']'))

dictionary = list(set(dictionary))
dictionary = sorted(dictionary)

os.chdir("../result")
with open('dic.txt', 'w') as f:
    for w in dictionary:
        f.write(w + '\n')
