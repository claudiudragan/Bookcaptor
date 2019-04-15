from xcaptor_tools.Book import Book, BulkReader
from xcaptor_tools.DocumentTermMatrix import DTM
from modules.Writer import Writer
from modules.Name import Name
from modules.Summary import Summarizer
from genrecaptor.modules.learner import Learner

if __name__ == "__main__":
    # writer = Writer(dtm, log=True, name="TestBooks")
    # writer.merge_results(character=False)
    dtm = None
    pred = None 
    count_vector = None

    print("Welcome to the console interface for Bookcaptor!\n")

    while True:
        print("\nSelect an option: \n")
        if dtm is None:
            print("1. Read input files from folder\n")
        print("2. Learner program for genre classification\n")
        if dtm is not None:
            print("3. List read documents\n")
            print("4. Summarize a document\n")
        print("9. Exit")

        inp = int(input("Selection: "))

        if inp == 1 and dtm is None:

            path = str(input("\nPath to document folder: "))
            out_name = str(input("Name for output files: "))
            bulk = BulkReader(path, log=True)
            readers = bulk.read_bulk()
            dtm = DTM(readers, log=True, name=out_name)

        elif inp == 2:
            if pred is None and count_vector is None:
                print("\nTraining...\n")
                learn = Learner("res/analysis_data/")
                pred, count_vector = learn.train_get_predictor()

            store = []

            inp_book = str(input("\nPath to book for classification: "))

            with open(inp_book, "r", encoding="utf-8") as book:
                cont = book.read()
                store.append(cont)

            print("\nThe book is: ")
            print(pred.predict(count_vector.transform(store)))

        elif inp == 3 and dtm is not None:
            
            for index, doc in enumerate(dtm.get_docs()):
                print("{0}. {1}".format(index, doc.get_name()))

        elif inp == 4 and dtm is not None:
            
            to_sum = int(input("Number of doc to summarize (from list at #3): "))
            summ = Summarizer(dtm, to_sum)

            sent_nr = int(input("How many sentences to print out: "))
            print("Summarizing...\n\n")
            sents = summ.summarize(sent_nr)

            for sent in sents:
                print(sent)

        elif inp == 9:
            print("\nGoodbye!")
            break
        
        