from modules.Reader import Reader
from modules.DocumentTermMatrix import DTM
from collections import OrderedDict


if __name__ == "__main__":
    red = Reader("res/data/JaneEyre_Plaintext.txt")
    dtmatrix = DTM(red)

    dtmatrix.make_histogram(0, top=20)
    dtmatrix.dtm_to_file(name="Jane_Eyre")