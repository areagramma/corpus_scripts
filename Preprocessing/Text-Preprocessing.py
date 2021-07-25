""" This file is a model for using AGStatistics.
Be sure to install spacy with your desired language using "python -m spacy download *spacy_model*"
(for more information go to https://spacy.io/models). For spacy documentation go to
https://spacy.io/usage/spacy-101. Other useful links for spacy are https://spacy.io/api/token#attributes &&
https://universaldependencies.org/docs/u/pos/
For pyphen (used for syllables) check https://pyphen.org/
"""

import os
import spacy
import pyphen
from AGStatistics import AGStatistics

files = os.listdir("Data/")  # Get all the names of the files from the "Data" folder
corpus = []
for file in files:
    with open("Data\\"+file, "rt", encoding="utf8") as fin:
        data = fin.read()
    corpus.append(data)
print(len(corpus))

pyphenModel = pyphen.Pyphen(lang='ro')  # Change to desired language
nlp = spacy.load("ro_core_news_lg")  # Change to desired model
myAGStatistics = AGStatistics(corpus, nlp, pyphenModel, True)
myAGStatistics.generate_statistics()
