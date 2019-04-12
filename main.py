from xcaptor_tools.Book import Book, BulkReader
from xcaptor_tools.DocumentTermMatrix import DTM
from modules.Writer import Writer
from modules.Name import Name
from modules.Summary import Summarizer

if __name__ == "__main__":
    inputPath = "res/data/input/"
    bulk = BulkReader(inputPath, log=True)
    readers = bulk.read_bulk()

    dtm = DTM(readers, log=True, name="TestBooks")
    
    summ = Summarizer(dtm, 1)

    sents = summ.summarize(10)

    i = 0
    for sent in sents:
        print(sent)
        print("===={0}====".format(i))
        i += 1
    
    # writer = Writer(dtm, log=True, name="TestBooks")
    # writer.merge_results(character=False)