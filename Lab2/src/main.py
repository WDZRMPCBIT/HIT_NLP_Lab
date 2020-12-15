from config import args
from utils.data import Paragraph


def set_random_seed(seed: int):
    """
    set random seed

    :param seed: random seed
    """
    import numpy
    import torch
    import random

    random.seed(seed)
    numpy.random.seed(seed)
    torch.random.manual_seed(seed)


if __name__ == '__main__':
    set_random_seed(args.random_seed)

    train = Paragraph(args.data_path + "/train.txt")
    valid = Paragraph(args.data_path + "/valid.txt")
    test = Paragraph(args.data_path + "/test.txt")
    t = train.package(300)
    print(len(t))
    """
    for word, slot in t:
        print(len(word))
        print(len(slot))
    """
