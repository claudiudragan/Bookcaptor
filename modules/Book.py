from string import punctuation
import time
from os import makedirs
import errno
from os import listdir
from os.path import isfile, join
from multiprocessing import Pool
import time


class Book:
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
            txt = self.gutenberg_clean(txt)

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

    def gutenberg_clean(self, txt):
        begin = txt.find("START OF THIS PROJECT GUTENBERG EBOOK")
        ending = txt.find("END OF THIS PROJECT GUTENBERG EBOOK")

        if begin != -1 and ending != -1:
            txt = txt[begin:ending]

        return txt

    def cleaner(self, word):
        word = word.lower()
        word = word.strip()
        quote = "«‹»›„‚“‟‘‛”’❛❜❟❝❞❮❯⹂〝〞〟＂‘"
        puncts = list(punctuation) + list(quote)

        if "\'s" in word:
            word = word.replace("'s", "")

        if "❜s" in word:
            word = word.replace("❜s", "")

        for punct in puncts:
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
                words.append(line.lower())

        return words

    def get_content(self):
        return self.content
    
    def get_name(self):
        return str(self.name)

    def get_raw(self):
        return self.raw

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return "<Reader class named: \"" + self.name + "\">"

class BulkReader:
    def __init__(self, ipPath, log=False):
        self.inputPath = ipPath
        self.log = log
    
    def read_one(self, book):
        reader = (Book(book, self.log))
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
