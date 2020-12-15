import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--random_seed',
                    '-rs',
                    type=int,
                    default=0,
                    help="random seed")

parser.add_argument('--data_path',
                    '-dp',
                    type=str,
                    default='../data',
                    help="path of data")
parser.add_argument('--model_path',
                    '-dp',
                    type=str,
                    default='../model',
                    help="path to save model")
parser.add_argument('--max_length',
                    '-ml',
                    type=int,
                    default=None,
                    help="max length to be processed")

parser.add_argument('--epoch', '-e', type=int, default=20, help="epoch")
parser.add_argument('--batch_size',
                    '-bs',
                    type=int,
                    default=500,
                    help="batch size")
parser.add_argument('--learning_rate',
                    '-lr',
                    type=float,
                    default=0.2,
                    help="learing rate")

args = parser.parse_args()
