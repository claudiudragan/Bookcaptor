import nltk

class Name:
    def __init__(self, book, init=False):
        if init:
            self.nltk_init()
        self.book = book

    def name_extractor(self):
        text = nltk.word_tokenize(self.book.raw)
        text = nltk.pos_tag(text)
        t = nltk.ne_chunk(text, binary=True)

        leaves = []

        for subtree in t.subtrees(filter=lambda x: x.label() == 'NE'):
            leaves.append(subtree.leaves())

        return leaves


    def nltk_init(self):
        nltk.download("punkt")
        nltk.download("maxent_ne_chunker")
        nltk.download("words")
        nltk.download("averaged_perceptron_tagger")
