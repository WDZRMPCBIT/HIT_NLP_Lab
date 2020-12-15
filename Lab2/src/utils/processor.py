from copy import deepcopy
from tqdm import tqdm
from typing import List

import numpy as np

import torch
from transformers import AdamW

from config import args
from utils.data import Paragraph
from utils.tokenizer import Tokenizer
from utils.metric import ExternalMetrics


class Processor(object):
    def __init__(self, model):
        """
        model process that can be trained and predicate

        :param model: model to use
        """
        self.__model = deepcopy(model)
        self.__tokenizer = Tokenizer()
        self.__optimizer = AdamW(model.parameters(), lr=args.learing_rate)
        self.__loss_function = torch.nn.NLLLoss()

    def train(self, dataset: Paragraph):
        """
        train model with dataset

        :param dataset: dataset used to train model
        """
        self.__model.train()

        for epoch in range(args.epoch):
            print("epoch" + str(epoch))
            batch = dataset.package(args.batch_size, True)

            for current_word, current_slot in tqdm(batch, ncols=len(batch)):
                word, span, mask = self.__wrap_word(current_word)
                slot = self.__exapnd_slot(current_slot)
                slot = torch.tensor(slot, dtype=torch.long)

                word = dataset.word_vocabulary().serialize(word)
                slot = dataset.slot_vocabulary().serialize(slot)

                predicate = self.__model(word, mask, span)
                loss = self.__loss_function(predicate, slot)

                self.__optimizer.zero_grad()
                loss.backward()
                self.__optimizer.step()

            torch.save(self.__model, args.model_path)

    def predicate(self, dataset: Paragraph, save_path: str = None) -> List[List[str]]:
        """
        predicate slot of sentences

        :param dataset: dataset to be predicated
        :param save_path: save result if not None
        """
        self.__model.eval()
        batch = dataset.package(args.batch_size, False)
        index = []

        for current_word, current_slot in tqdm(batch, ncols=len(batch)):
            word, span, mask = self.__wrap_word(current_word)
            slot = self.__exapnd_slot(current_slot)
            slot = torch.tensor(slot, dtype=torch.long)

            word = dataset.word_vocabulary().serialize(word)
            slot = dataset.slot_vocabulary().serialize(slot)

            predicate = self.__model(word, mask, span)
            index += predicate

        result = [[]] * len(index)
        for i in range(len(result)):
            for j in range(len(result[i])):
                result[i].append(dataset.slot_vocabulary().get(index[i][j]))

        if save_path is not None:
            with open(save_path) as f:
                f.write("-DOCSTART- -X- -X- O" + "/n" + "/n")

        return result

    def estimate(self, dataset: Paragraph):
        """
        calc accuracy and F1

        :param predicate:
        :param real:
        """
        predicate = self.predicate(dataset)
        real = dataset.slot()

        acc = ExternalMetrics.accuracy(predicate, real)
        f1 = ExternalMetrics.f1_score(predicate, real)

        return acc, f1

    def __wrap_word(self, batch: List[List[str]]):
        """
        change word batch to piece batch,
        and padding the result
        """
        piece, span = self.__tokenizer(batch)
        piece = self.__add_padding_cls_sep(piece)

        index = [self.__tokenizer.piece2index(x) for x in piece]
        index = torch.tensor(index, dtype=torch.long)

        mask = torch.tensor(np.where(index != 0, 1, 0))

        return index, span, mask
