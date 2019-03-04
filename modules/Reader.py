from string import punctuation
from .PorterStemmer import PorterStemmer
import time

class Reader:
    def __init__(self, rfile, log=False, keep_raw=False):
        self.log = log
        self.stopwords = self.load_stopwords()
        self.stemmer = PorterStemmer()
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

            #results = [self.cleaner(word) for word in content if word not in self.stopwords]
            #results = [self.stemmer.stem(word, 0, len(word)-1) for word in results]
            #results = [word for word in results if word not in self.stopwords]

            #for item in results:
            #    for punct in list(punctuation):
            #        item = item.replace(punct, "")

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
        
        #word = self.stemmer.stem(word, 0, len(word)-1)
        if word not in self.stopwords:
            return word
        else:
            return None

    def load_stopwords(self):
        words = []
        with open("res/stop.txt", encoding="utf-8") as stops:
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