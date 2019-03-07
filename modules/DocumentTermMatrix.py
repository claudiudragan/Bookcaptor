from collections import OrderedDict, Counter
import numpy
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from os import linesep
import csv
import time

class DTM:
    def __init__(self, docs, log=False):
        self.docs = []
        self.log = log
        for doc in docs:
            self.docs.append(doc)
        self.name = "default"
        self.matrix = self.create_matrix()

    def create_matrix(self):
        start = time.time()
        # words = []
        matrix = []

        for doc in self.docs:
            count = Counter(doc.content)
            matrix.append(count)


        # #TODO Optimize matrix creation!
        # for doc in self.docs:  
        #     freq = {}
        #     for word in doc.content:
        #         if word not in words:
        #             words.append(word)
        #             freq[word] = 1
        #         else:
        #             freq[word] += 1
        #     matrix.append(freq)

        # #TODO Change padding method
        # if len(self.docs) > 1:
        #     for e in matrix:
        #         for f in matrix:
        #             if len(e) < len(f):
        #                 while len(e) < len(f):
        #                     e.append(0)
        #             elif len(e) > len(f):
        #                 while len(e) > len(f):
        #                     f.append(0)

        end = time.time()
        t = end - start

        if self.log:
            print("[LOG] Created DTMatrix in {0:.2f} seconds.".format(t))

        return matrix

    def dtm_to_file(self, name=None):
        if name is None:
            name = self.name

        with open("res/data/results/{0}_matrix.csv".format(name), "w+", encoding="utf-8") as w:
            writer = csv.writer(w, delimiter=",")
            
            s = set()
            for count in self.matrix:
                s.update(count.keys())
            print(list(s)[:20])

            writer.writerow(s)
            colsep = ','
            def writecol(string):
                w.write(str(string))
                w.write(colsep)

            index = 0
            for doc in self.docs:
                writecol(doc.name)
                w.write(linesep)
                
                for word in s:
                    writecol(self.matrix[index].get(word, '0'))
                
                w.write(linesep)
                index += 1

            # i = 0
            # for count in self.matrix:
            #     w.write(self.docs[i].name + linesep)
            #     writer.writerow(l)
            #     i += 1
        
        if self.log:
            print("[LOG] Successfully printed data to res/data/results/{0}_matrix.csv".format(name))


    def get_matrix(self):
        return self.matrix