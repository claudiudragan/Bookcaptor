import nltk
from collections import Counter
import time

class Name:
    def __init__(self, book, init=False, log=False):
        if init:
            self.nltk_init()
        self.book = book
        self.log = log

        start = time.time()
        self.leaves = self.name_extractor()
        self.names = self.name_cleaner()
        end = time.time()

        if log:
            print("[LOG] Finished NER for {0} in {1:.2f}s".format(self.book.get_name(), end - start))
        

    def name_extractor(self):
        text = nltk.word_tokenize(self.book.raw)
        text = nltk.pos_tag(text)
        t = nltk.ne_chunk(text, binary=True)

        leaves = []

        for subtree in t.subtrees(filter=lambda x: x.label() == 'NE'):
            leaves.append(subtree.leaves())

        return leaves

    def count_names(self):
        count = Counter(self.names)
        count = sorted(count.items(), key=lambda kv: kv[1], reverse=True)

        chars = []
        for name in count[:15]:
            chars.append(name)

        return chars
    
    def name_cleaner(self):
        names = []
        for lists in self.leaves:
            name = ""
            step = 0
            for l in lists:
                if step == 0:
                    name += "{0} ".format(l[0])
                    step = 1
                else:
                    name += l[0]
            step = 0
            names.append(name)

        return names

    def nltk_init(self):
        nltk.download("punkt")
        nltk.download("maxent_ne_chunker")
        nltk.download("words")
        nltk.download("averaged_perceptron_tagger")
