class Summarizer:
    def __init__(self, dtm, index):
        self.index = index
        self.dtm = dtm
        self.vec = dtm.get_matrix()[index]

    def normalize_freq(self):
        maximum = float(self.vec.most_common()[0][1])
        normalized_freqs = {}

        for key in self.vec:
            normalized_freqs[key] = self.vec[key]/maximum

        return normalized_freqs

    def summarize(self, sent_nr):
        sents = self.dtm.get_sentences(self.index)
        freq = self.normalize_freq()

        ranks = {}

        i = 0
        for sent in sents:
            sent.rstrip()
            ranks[i] = 0
            for word in sent.split():
                if word in freq:
                    ranks[i] += freq[word]
            i += 1

        top = self.get_top_sents(ranks, sent_nr)
        top_sents = [sents[i] for i in top]

        return top_sents

    def get_top_sents(self, ranks, sent_nr):
        return sorted(ranks, key=ranks.get, reverse=True)[:sent_nr]


        


