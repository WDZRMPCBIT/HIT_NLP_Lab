from config import args
from paragraph import Paragraph
from vocabulary import Vocabulary

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

    if args.multiple_process:
        from tokenizer.multi_process import MultiProcess
        tokenizer = MultiProcess(tokenizer)

    paragraph = Paragraph.load(args.data_path, False, args.max_line)
    paragraph.tokenize(tokenizer)
    paragraph.save(args.result_path)
