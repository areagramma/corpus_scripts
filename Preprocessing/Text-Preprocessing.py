# Read all the data
import os
from AGStatistics import AGStatistics
os.chdir("E:/Area Gramma/Corpus/Spacy/Subs")  # The folder containing the subs
files = os.listdir()  # Get all the names of the files
inputPath = "E:/Area Gramma/Corpus/Spacy/Subs"

corpus = []
for file in files:
    fin = open(inputPath+'\\'+file, "rt", encoding="utf8")
    data = fin.read()
    corpus.append(data)
    fin.close()
print(len(corpus))

myAGStatistics = AGStatistics(corpus, True)
myAGStatistics.generate_statistics()
