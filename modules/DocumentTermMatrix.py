from collections import OrderedDict
import numpy
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from os import linesep
import csv
import time

class DTM:
    def __init__(self, *docs, log=False):
        self.docs = []
        self.log = log
        for doc in docs:
            self.docs.append(doc)
        self.name = "default"
        self.matrix, self.words = self.create_matrix()

    def create_matrix(self):
        start = time.time()
        words = []
        matrix = []

        #TODO Optimize matrix creation!
        for doc in self.docs:  
            freq = {}
            for word in doc.content:
                if word not in words:
                    words.append(word)
                    freq[word] = 1
                else:
                    freq[word] += 1
            matrix.append(freq)

        #TODO Change padding method
        if len(self.docs) > 1:
            for e in matrix:
                for f in matrix:
                    if len(e) < len(f):
                        while len(e) < len(f):
                            e.append(0)
                    elif len(e) > len(f):
                        while len(e) > len(f):
                            f.append(0)

        end = time.time()
        t = end - start

        if self.log:
            print("[LOG] Created DTMatrix in {0:.2f} seconds.".format(t))

        return matrix, words

    def dtm_to_file(self, name=None):
        if name is None:
            name = self.name

        with open("res/data/results/{0}_matrix.csv".format(name), "w+", encoding="utf-8") as w:
            writer = csv.writer(w, delimiter=",")
            writer.writerow(self.words)
            
            i = 0
            for l in self.matrix:
                w.write(self.docs[i].name + linesep)
                writer.writerow(l)
                i += 1
        
        if self.log:
            print("[LOG] Successfully printed data to res/data/results/{0}_matrix.csv".format(name))


    def get_matrix(self):
        return self.matrix
    def get_words(self):
        return self.words