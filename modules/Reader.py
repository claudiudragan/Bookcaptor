from string import punctuation
import time
from os import makedirs
import errno
from os import listdir
from os.path import isfile, join
from multiprocessing import Pool
import time


class Reader:
    def __init__(self, rfile, log=False, keep_raw=True):
        try:
            makedirs("res/data/results/")
        except FileExistsError:
            pass
        self.log = log
        self.stopwords = self.load_stopwords()
        self.content, self.raw = self.load_content(rfile, keep_raw)
        self.name = rfile[rfile.rfind("/") + 1:rfile.rfind(".")]
        
    
    def load_content(self, f, keep_raw):
        start = time.time()
        with open(f, "r", encoding="utf-8") as text:
            txt = text.read()
            content = txt.replace("--", " ")
            content = content.split()
            results = []

            for word in content:
                word = self.cleaner(word)
                if word is not None:
                        results.append(word)

            end = time.time()
            t = end - start
            if self.log:
                print("[LOG] Loaded text ({0}) in {1:.2f} seconds.".format(f, t))

            if keep_raw:
                return results, txt
            else:
                del txt
                return results, None

    def cleaner(self, word):
        word = word.lower()
        word = word.strip()

        if word[-2:] == "'s":
            word = word.replace("'s", "")

        for punct in list(punctuation):
            word = word.replace(punct, "")
        
        if word not in self.stopwords and not word == "":
            return word
        else:
            return None


    def load_stopwords(self):
        words = []
        with open("res/data/stop.txt", encoding="utf-8") as stops:
            for line in stops:
                line = line.strip()
                words.append(line)

        return words

    def get_content(self):
        return self.content

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return "<Reader class named: \"" + self.name + "\">"

class BulkReader:
    def __init__(self, ipPath):
        self.inputPath = ipPath
    
    def read_one(self, book):
        reader = (Reader(book, log=True))
        return reader

    def read_bulk(self):
        books = [(self.inputPath + f) for f in listdir(self.inputPath) if isfile(join(self.inputPath, f))]
        readers = []
        pool = Pool(4)

        begin = time.time()
        readers = pool.map(self.read_one, books)
        pool.close()
        pool.join()
        end = time.time()

        print("[LOG] Read all input in {0:.2f}s".format(end-begin))
        return readers
