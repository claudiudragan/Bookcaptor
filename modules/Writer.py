from collections import OrderedDict
import numpy
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
import io
from os import remove

class Writer:
    def __init__(self, DocumentTermMatrix, log=False, name="default"):
        font = {
            'family' : 'Arial',
            'weight' : 'bold',
            'size'   : 12
        }

        matplotlib.rc('font', **font) 
        
        self.DTM = DocumentTermMatrix
        self.log = log
        self.name = name
        self.size = letter
        self.create_pdf()

    def make_histogram(self, doc_index, top=10):
        d = self.create_ordered(doc_index)
        values = list(d.values())
        keys = list(d.keys())

        plt.bar(values[:top], keys[:top])
        plt.show()

    def create_pdf(self):
        title = "{0} Analysis Results".format(self.name)
        gener = "Generated by Bookcaptor"
        can = canvas.Canvas("res/data/results/{0}_Title.pdf".format(self.name), pagesize=letter)
        
        can.setFont("Helvetica-Bold", 28)
        can.setAuthor("Bookcaptor")
        can.setTitle(title)
        
        can.drawString((self.size[0] - can.stringWidth(title))/2, self.size[1] - 90, title.replace("_", " "))

        can.setFont("Helvetica", 18)
        can.drawString(((self.size[0] - can.stringWidth(gener))/2), self.size[1] - 118, gener)

        can.setFont("Helvetica", 10)
        can.drawString((self.size[0] - can.stringWidth("1"))/2, 30, "1")

        can.showPage()
        can.save()

    def histogram_to_pdf(self, doc_index, top=10):
        d = self.create_ordered(doc_index)
        values = list(d.values())
        keys = list(d.keys())

        fig = plt.figure(figsize=(8.5, 11.0))
        plt.bar(values[:top], keys[:top])
        plt.title("Histogram of the {0} most common words".format(top))
 
        fig.savefig("res/data/results/{0}_hist.pdf".format(self.name))

        merger = PdfFileMerger()
        merger.append("res/data/results/{0}_Title.pdf".format(self.name))
        merger.append("res/data/results/{0}_Hist.pdf".format(self.name))
        merger.write("res/data/results/{0}_Results.pdf".format(self.name))   

        merger.close() 

        try:
            remove("res/data/results/{0}_Title.pdf".format(self.name))
            remove("res/data/results/{0}_Hist.pdf".format(self.name))
        except OSError:
            pass


    
    def create_ordered(self, doc_index):
        d = dict(zip(self.DTM.matrix[doc_index], self.DTM.words))
        d = OrderedDict(sorted(d.items(), reverse=True))

        return d
