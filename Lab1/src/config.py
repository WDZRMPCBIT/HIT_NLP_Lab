import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--data_path',
                    '-dp',
                    type=str,
                    default="../data/199801_sent.txt",
                    help="数据集路径")
parser.add_argument('--vocabulary_path',
                    '-vp',
                    type=str,
                    default="../result/dic.txt",
                    help="词典路径")
parser.add_argument('--result_path',
                    '-rp',
                    type=str,
                    default="../result",
                    help="输出路径")
parser.add_argument('--standard_path',
                    '-sp',
                    type=str,
                    default="../result/simplified.txt",
                    help="分词标准路径")
parser.add_argument('--output_path',
                    '-op',
                    type=str,
                    default="../result/score.txt",
                    help="评估结果输出路径")
parser.add_argument('--tokenizer',
                    '-t',
                    type=str,
                    default="segmentation",
                    help="分词器类型")
parser.add_argument('--multiple_process',
                    '-mp',
                    type=bool,
                    default=True,
                    help="启用多进程")
parser.add_argument('--storage',
                    '-s',
                    type=str,
                    default="trie",
                    help="词典组织结构")
parser.add_argument('--max_line',
                    '-ml',
                    type=int,
                    default=100,
                    help="处理文件最大行数")
parser.add_argument('--max_gram',
                    '-mg',
                    type=int,
                    default=2,
                    help="组成词组的最大单词数")

args = parser.parse_args()
