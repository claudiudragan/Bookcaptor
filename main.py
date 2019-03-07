from modules.Reader import Reader, BulkReader
from modules.DocumentTermMatrix import DTM
from modules.Writer import Writer

if __name__ == "__main__":
    inputPath = "res/data/input/"
    bulk = BulkReader(inputPath)
    readers = bulk.read_bulk()

    dtm = DTM(readers)
    dtm.dtm_to_file()
