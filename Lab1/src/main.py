from config import args
from paragraph import Paragraph
from vocabulary import Vocabulary
from estimate import esitmate

if __name__ == "__main__":
    if args.storage == "binary_linear_list":
        from storage.binary_linear import BinaryLinearList
        storage = BinaryLinearList(args.max_gram)
    if args.storage == "linear_list":
        from storage.linear import LinearList
        storage = LinearList()
    if args.storage == "hash_bucket":
        from storage.hash_bucket import HashBucket
        storage = HashBucket()
    vocabulary = Vocabulary.load(args.vocabulary_path, args.max_gram, storage)

    if args.tokenizer == "forward":
        from tokenizer.forward import Forward
        tokenizer = Forward(vocabulary)
    if args.tokenizer == "backward":
        from tokenizer.backward import Backward
        tokenizer = Backward(vocabulary)
    if args.tokenizer == "segmentation":
        from tokenizer.segmentation import OmniSegmentation
        tokenizer = OmniSegmentation(vocabulary)

    if args.multiple_process:
        from tokenizer.multi_process import MultiProcess
        tokenizer = MultiProcess(tokenizer)

    paragraph = Paragraph.load(args.data_path, False, args.max_line)
    paragraph.tokenize(tokenizer)
    paragraph.save(args.result_path)

    precision, callback, F1 = esitmate(args.result_path, args.standard_path)
    with open(args.output_path, 'a') as f:
        f.write("tokenizer: " + args.tokenizer + "\n")
        f.write("multi-process: " + str(args.multiple_process) + "\n")
        f.write("storage: " + args.storage + "\n")
        f.write("max gram: " + str(args.max_gram) + "\n")
        f.write("precision: " + str(precision) + "\n")
        f.write("callback: " + str(callback) + "\n")
        f.write("F1: " + str(F1) + "\n")
        f.write("\n")
