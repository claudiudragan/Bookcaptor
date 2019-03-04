# Bookcaptor
**Bookcaptor** is a text mining and analysis written in Python 3.6 which aims to be a tool for reading text files and extracting various statistics from them.
Currently only supports *.txt* files, with support for more filetypes to be implemented in the future along with support for more complex output file types (ie. PDFs).

### Twitter
Before using the twitter functionality you must also install *tweepy* using:
```
python -m pip install tweepy
```

To use the Twitter app insert your own app credentials in a file called "tweet_auth.txt" in res/ like so:
```
consumer_key=
consumer_secret=
access_key=
access_secret=
```

After which you can run *getTweet.py* from the modules folder like you would any Python script:
```
python getTweet.py
```
Yes, it's a bit unprofessional. I'll clean it up later.

### Dependencies
Bookcaptor has been tested on Python 3.6 and requires only *matplotlib* at the moment which can be installed using:
```
python -m pip install matplotlib
```

### Bibliography
```
Lexicon used for sentiment analysis: http://mpqa.cs.pitt.edu/lexicons/subj_lexicon/

Stopword list: https://www.ranks.nl/stopwords

Porter Stemmer implementation from: https://tartarus.org/martin/PorterStemmer/python.txt

Books used for data from: https://www.gutenberg.org/
```