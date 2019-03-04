from collections import OrderedDict
import numpy
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from os import makedirs
import errno

class DTM:
    def __init__(self, *docs):
        self.docs = []
        for doc in docs:
            self.docs.append(doc)
        self.name = "default"
        self.matrix, self.words = self.create_matrix()

    def create_matrix(self):
        words = []
        matrix = []
        for doc in self.docs:  
            freq = []
            for word in doc.content:
                if word not in words:
                    words.append(word)
                    freq.append(1)
                else:
                    freq[words.index(word)] += 1
            matrix.append(freq)

        #TODO Change padding method
        for e in matrix:
            for f in matrix:
                if len(e) < len(f):
                    while len(e) < len(f):
                        e.append(0)
                elif len(e) > len(f):
                    while len(e) > len(f):
                        f.append(0)

        return matrix, words

    def make_histogram(self, doc_index, top=10):
        d = dict(zip(self.matrix[doc_index], self.words))
        d = OrderedDict(sorted(d.items(), reverse=True))
        values = list(d.values())
        keys = list(d.keys())

        plt.bar(values[:top], keys[:top])
        plt.show()

    def dtm_to_file(self, name=None):
        if name is None:
            name = self.name

        try:
            makedirs("res/data/results/")
        except FileExistsError:
            pass

        with open("res/data/results/{0}_matrix.txt".format(name), "w+", encoding="utf-8") as w:
            w.write("[WORDS] [")
            for word in self.words:
                w.write("{0} ".format(word))
            w.write("]\n")
            i = 0
            for l in self.matrix:
                w.write("[{0}] [".format(self.docs[i].name))
                for item in l:
                    w.write("{0} ".format(item))
                w.write("]") 
                i += 1


    def get_matrix(self):
        return self.matrix
    def get_words(self):
        return self.words