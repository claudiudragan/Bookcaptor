from collections import OrderedDict
import numpy
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages
from PyPDF2 import PdfFileWriter, PdfFileReader

class Writer:
    def __init__(self, DocumentTermMatrix, log=False):
        font = {
            'family' : 'Arial',
            'weight' : 'bold',
            'size'   : 12
        }

        matplotlib.rc('font', **font) 
        
        self.DTM = DocumentTermMatrix
        self.log = log

    def make_histogram(self, doc_index, top=10):
        d = self.create_ordered(doc_index)
        values = list(d.values())
        keys = list(d.keys())

        plt.bar(values[:top], keys[:top])
        plt.show()

    def create_pdf(self, name=None):
        if name is None:
            name = "default"
        
        with open("res/data/results/{0}.pdf".format(name), "wb+") as f:
            pdfw = PdfFileWriter()
            pdfw.addBlankPage(8.3, 11.7)
            pdfw.write(f)

    def histogram_to_pdf(self, doc_index, top=10, name=None):
        if name is None:
            name = "default"

        d = self.create_ordered(doc_index)
        values = list(d.values())
        keys = list(d.keys())

        plt.bar(values[:top], keys[:top])

        fig = plt.figure(figsize=(10,10), dpi=100)
        plt.bar(values[:top], keys[:top])
        plt.title("Histogram of the {0} most common words".format(top))
 
        fig.savefig("res/data/results/{0}.pdf".format(name), bbox_inches="tight")

        if self.log:
            print("[LOG] Successfully saved histogram to {0}.pdf".format(name))
    
    def create_ordered(self, doc_index):
        d = dict(zip(self.DTM.matrix[doc_index], self.DTM.words))
        d = OrderedDict(sorted(d.items(), reverse=True))

        return d
