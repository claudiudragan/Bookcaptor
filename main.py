from modules.Reader import Reader
from modules.DocumentTermMatrix import DTM
from modules.Writer import Writer
from collections import OrderedDict


if __name__ == "__main__":
    red = Reader("res/data/JaneEyre_Plaintext.txt", log=True)
    dtmatrix = DTM(red, log=True)
    writer = Writer(dtmatrix, log=True, name="Jane_Eyre")

    writer.histogram_to_pdf(0)
    #dtmatrix.dtm_to_file(name="Jane_Eyre")