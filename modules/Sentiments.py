class Sentiments:
    def __init__(self):
        self.negative = []
        self.positive = []
        self.neutral = []

        with open("res/data/subjclueslen1-HLTEMNLP05.tff") as f:
            for line in f:
                beg = line.find("word1") + 6
                end = line.find("pos1")
                word = line[beg:end]
                word = word.rstrip()

                polarpos = line.find("priorpolarity") + 14
                polar = line[polarpos:]
                polar = polar.rstrip()

                if polar == 'positive':
                    self.positive.append(word)         
                elif polar == 'negative':
                    self.negative.append(word)
                else:
                    self.neutral.append(word)

        self.positive = list(set(self.positive))
        self.negative = list(set(self.negative))
        self.neutral = list(set(self.neutral))
        

    def getPositive(self):
        return self.positive
    
    def getNegative(self):
        return self.negative
    
    def getNeutral(self):
        return self.neutral

