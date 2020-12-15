from typing import List, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F
from transformers import BertModel


class BertRecognizer(nn.Module):
    def __init__(self, slot_vocab_size: int, dropout_rate: float):
        super(BertRecognizer, self).__init__()
        self.__encoder = BertEncoder(dropout_rate)
        self.__decoder = LinearDecoder(BertEncoder.encoder_dim,
                                       slot_vocab_size)
        self.__piece2word = Piece2Word()

    def forward(self, piece_tensor: torch.Tensor, piece_mask,
                span_list: List[List[Tuple[int, int]]]):
        """
        encoder-decoder 模型的前向过程.

        :param piece_mask:
        :param piece_tensor: 是 piece 级别分词的列表.
        :param span_list: 是 piece 对应原 word 的标识表.
        :return: 返回一个 batch 对应 intent 的预测分布.
        """
        # 调用基于bert的encoder层，得到hidden
        # hidden：（batch_size，max_piece_len，768）
        hidden = self.__piece_encoder(piece_tensor, piece_mask)

        # 将表示 piece 的张量合并成 word 的张量.span[i]+1是因为跳过前面的CLS
        span_tensor_list = [[
            self.__piece2word(hidden[[sent_i], span[0] + 1:span[1] + 1, :])
            for span in span_list[sent_i]
        ] for sent_i in range(0, len(span_list))]

        # span_tensor_list:(batch_size，max_word_len，768)
        # 对合成之后的张量列表做 padding.
        len_list = self.__padding(span_tensor_list,
                                  torch.zeros((1, 1, hidden.size(2))))

        # 转换成tensor
        # padded_tensor : [batch_size, max_len, 768]
        padded_tenor = torch.cat([
            torch.cat(span_tensor_list[sent_i], dim=1)
            for sent_i in range(0, len(span_list))
        ],
                                 dim=0)

        # 送给decoder层预测
        # [batch_size, max_len, 768]==>[batch_size, max_len, slot_vocab_size]
        slot_tensor = self._slot_decoder(padded_tenor)

        # slot将不是pad的部分（即word部分）的预测连接起来
        return torch.cat(
            [slot_tensor[i][:len_list[i], :] for i in range(0, len(len_list))],
            dim=0)

    @staticmethod
    def __padding(seq_list: List[List[torch.Tensor]], pad_sign):
        """
        对输入张量二维表做 padding, 且不改变对象引用.
        """

        len_list: list = [len(seq) for seq in seq_list]
        max_len: int = max(len_list)

        if torch.cuda.is_available():
            pad_sign = pad_sign.cuda()

        for seq_i in range(0, len(len_list)):
            seq_list[seq_i].extend([pad_sign] * (max_len - len_list[seq_i]))

        return len_list


class BertEncoder(nn.Module):
    """
    num_layer = 12
    encoder_dim = 768
    """
    def __init__(self,
                 dropout_rate: float,
                 model_type: str = "bert-base-uncased"):
        super(BertEncoder, self).__init__()
        self._model = BertModel.from_pretrained(model_type)
        self._dropout = nn.Dropout(dropout_rate)

    def forward(self, piece_tensor: torch.LongTensor, mask):
        hidden = self._model(piece_tensor, attention_mask=mask)[0]
        hidden = self._dropout(hidden)

        return hidden


class LinearDecoder(nn.Module):
    def __init__(self, input_dim: int, output_dim: int):
        super(LinearDecoder, self).__init__()
        self._linear_layer = nn.Linear(input_dim, output_dim)

    def forward(self, hidden):
        return F.log_softmax(self._linear_layer(hidden), dim=-1)


class Piece2Word(nn.Module):
    def __init__(self):
        super(Piece2Word, self).__init__()

    def forward(self, input_tensor):
        return self._first(input_tensor)

    @staticmethod
    def _first(input_tensor):
        return input_tensor[:, 0, :].view(1, 1, -1)

    @staticmethod
    def _average(input_tensor):
        return torch.mean(input_tensor, dim=1, keepdim=True)

    @staticmethod
    def _sum(input_tensor):
        return torch.sum(input_tensor, dim=1, keepdim=True)
