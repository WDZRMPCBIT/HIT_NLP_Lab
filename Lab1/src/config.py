import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--data_path', '-dp', type=str,
                    default="../data/199801_sent.txt", help="数据集路径")
parser.add_argument('--vocabulary_path', '-vp', type=str,
                    default="../result/dic.txt", help="词典路径")
parser.add_argument('--result_path', '-rp', type=str,
                    default="../result/forward.txt", help="输出路径")
parser.add_argument('--tokenizer', '-t', type=str,
                    default="forward", help="分词器类型")
parser.add_argument('--storage', '-s', type=str,
                    default="linear_list", help="词典组织结构")
parser.add_argument('--max_line', '-ml', type=int, default=10, help="处理文件最大行数")
parser.add_argument('--max_length', '-mal', type=int,
                    default=1, help="组成词组的最大单词数")

args = parser.parse_args()
