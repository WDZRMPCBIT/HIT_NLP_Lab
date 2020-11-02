from phrase import Phrase


class Trie:
    def __init__(self):
        self.__root = {}

    def add(self, phrase: Phrase):
        """
        向Trie中添加一个词组

        :param phrase: 待添加的词组
        """
        node = self.__root
        phrase = phrase.phrase()

        for s in phrase:
            if s in node.keys():
                node = node[s]
            else:
                node[s] = {}
                node = node[s]
        node['is_word'] = True

    def get(self, phrase: Phrase):
        """
        Returns if the word is in the trie.
        """
        node = self.__root
        phrase = phrase.phrase()

        for s in phrase:
            if s in node.keys():
                node = node[s]
            else:
                return False

        if 'is_word' in node.keys():
            return True
        else:
            return False
