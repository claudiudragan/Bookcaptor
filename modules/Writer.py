from collections import OrderedDict
import numpy
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

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

        self.create_pdf()

    def make_histogram(self, doc_index, top=10):
        d = self.create_ordered(doc_index)
        values = list(d.values())
        keys = list(d.keys())

        plt.bar(values[:top], keys[:top])
        plt.show()

    def create_pdf(self):
        doc = SimpleDocTemplate("{0}.pdf".format(self.name), pagesize=letter, rightMargin=72,leftMargin=72,
              topMargin=72,bottomMargin=18)

        styles = getSampleStyleSheet()     
        styles.add(ParagraphStyle(name="Justify", alignment=TA_JUSTIFY)) 
        Story = []
        text = '''
                    <title>{0} Analysis Results<title><br/>
                '''.format(self.name)

        Story.append(Paragraph(text, styles["Normal"]))
        doc.build(Story)

    def histogram_to_pdf(self, doc_index, top=10):
        d = self.create_ordered(doc_index)
        values = list(d.values())
        keys = list(d.keys())

        plt.bar(values[:top], keys[:top])

        fig = plt.figure(figsize=(10,10), dpi=100)
        plt.bar(values[:top], keys[:top])
        plt.title("Histogram of the {0} most common words".format(top))
 
        fig.savefig("res/data/results/{0}_hist.pdf".format(self.name), bbox_inches="tight")

        if self.log:
            print("[LOG] Successfully saved histogram to {0}_hist.pdf".format(self.name))
        
        merger = PdfFileMerger()
        merger.append("res/data/results/{0}.pdf".format(self.name))
        merger.append("res/data/results/{0}_hist.pdf".format(self.name))
        merger.write("res/data/results/{0}.pdf".format(self.name))    

    
    def create_ordered(self, doc_index):
        d = dict(zip(self.DTM.matrix[doc_index], self.DTM.words))
        d = OrderedDict(sorted(d.items(), reverse=True))

        return d
