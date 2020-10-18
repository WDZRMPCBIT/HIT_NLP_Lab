from config import args
from paragraph import Paragraph
from vocabulary import Vocabulary

if __name__ == "__main__":
    if args.storage == "linear_list":
        from storage.linear import LinearList
        storage = LinearList()
    vocabulary = Vocabulary.load(
        args.vocabulary_path, args.max_length, storage)

    print(vocabulary.get("迈向"))

    if args.tokenizer == "forward":
        from tokenizer.forward import forward
        tokenizer = forward(vocabulary)
    paragraph = Paragraph.load(args.data_path, False, args.max_line)
    paragraph.tokenize(tokenizer)
    paragraph.save(args.result_path)
