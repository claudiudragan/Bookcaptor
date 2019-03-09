# Bookcaptor
**Bookcaptor** is a text mining and analysis written in Python 3.6 which aims to be a tool for reading text files and extracting various statistics from them.
Currently only supports *.txt* files, with support for more filetypes to be implemented in the future.
The output is given as a PDF file displaying a variety of statistics about the chosen documents (ie. books) which can be found in the *res/data/results/* folder.

### Dependencies
Bookcaptor has been tested on Python 3.6 and requires *matplotlib*, *reportlab*, *NLTK*, and *PyPDF2* at the moment which can be installed using:
```
python -m pip install matplotlib
python -m pip install reportlab
python -m pip install NLTK
python -m pip install PyPDF2
```

### Bibliography
```
Lexicon used for sentiment analysis: http://mpqa.cs.pitt.edu/lexicons/subj_lexicon/

Stopword list: https://www.ranks.nl/stopwords

Books used for data from: https://www.gutenberg.org/
```

### Twitter
Currently the Twitter module only exists as a stub. Bookcaptor does not support convenient tweet analysis at the moment though getTweet.py can be used to grab a set of tweets using a certain keyword.