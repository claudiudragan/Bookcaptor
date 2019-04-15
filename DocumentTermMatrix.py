from collections import OrderedDict, Counter
import numpy
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize
from os import linesep
import csv
import time

class DTM:
    def __init__(self, docs, log=False, name="Default"):
        self.docs = []
        self.log = log
        for doc in docs:
            self.docs.append(doc)
        self.name = name
        self.len = len(docs)
        self.matrix = self.create_matrix()

    def create_matrix(self):
        start = time.time()
        matrix = []

        for doc in self.docs:
            count = Counter(doc.content)
            matrix.append(count)

        end = time.time()

        if self.log:
            print("[LOG] Created DTMatrix in {0:.2f} seconds.".format(end-start))

        return matrix

    def dtm_to_file(self):
        with open("res/data/results/{0}_Matrix.csv".format(self.name), "w+", encoding="utf-8") as w:
            writer = csv.writer(w, delimiter=",")
            
            #make a set of words so that each appears only once
            s = set()
            for count in self.matrix:
                s.update(count.keys())

            writer.writerow(s)
            colsep = ','
            def writecol(string):
                w.write(str(string))
                w.write(colsep)

            index = 0
            for doc in self.docs:
                writer.writerow(doc.name)
                
                #iter through the set and get the wordcount from the matrix or 0
                for word in s:
                    writecol(self.matrix[index].get(word, '0'))
                
                w.write(linesep)
                index += 1
        
        if self.log:
            print("[LOG] Successfully printed data to res/data/results/{0}_Matrix.csv".format(self.name))


    def make_index_vec(self):
        keys = set()
        values = []
        names = []

        for count in self.matrix:
            keys.update(count.keys())

        index = 0
        for doc in self.docs:
            names.append(doc.name)
            values.append([])

            for word in keys:
                values[index].append(self.matrix[index].get(word, 0))
            index += 1

        return (names, keys, values)

    def get_sentences(self, index):
        doc = self.docs[index].get_raw()

        return sent_tokenize(doc)

    def get_matrix(self):
        return self.matrix
    
    def get_doc(self, index):
        return self.docs[index]
    
    def get_docs(self):
        return self.docs

