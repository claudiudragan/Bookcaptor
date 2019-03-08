from modules.Book import Book, BulkReader
from modules.DocumentTermMatrix import DTM
from modules.Writer import Writer

if __name__ == "__main__":
    inputPath = "res/data/input/"
    bulk = BulkReader(inputPath, log=True)
    readers = bulk.read_bulk()

    dtm = DTM(readers, log=True, name="TestBooks")
    dtm.dtm_to_file()

    writer = Writer(dtm, log=True, name="TestBooks")
    writer.histograms_to_pdf()