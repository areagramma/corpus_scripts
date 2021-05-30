#Read all the data
import os
from langdetect import detect
os.chdir("E:\Area Gramma\Corpus\Spacy\Subs") #The folder containing the subs
files = os.listdir() #Get all the names of the files

inputPath = "E:\Area Gramma\Corpus\Spacy\Subs"

corpus = []
for file in files:
    fin = open(inputPath+'\\'+file, "rt", encoding="utf8")
    data = fin.read()
    if (detect(data) == 'ro'):
        corpus.append(data)
    fin.close()
print(len(corpus))




#Preprocessing && statistics
import spacy

lemmasDictionary = dict()
tokensDictionary = dict()
punctuationsDictionary = dict()
nlp = spacy.load("ro_core_news_lg")

i = 0
numberOfSentences = 0
while i < 150:
    data = corpus[i]
    data = data.lower()
    print(i)
    doc = nlp(data)
    for token in doc:
        if token.pos_ == 'PUNCT' or token.text == '\n':
            if token.text not in punctuationsDictionary:
                punctuationsDictionary[token.text] = 1
            else:
                punctuationsDictionary[token.text] += 1
        else:
            if token.lemma_ not in lemmasDictionary:
                lemmasDictionary[token.lemma_] = 1
            else:
                lemmasDictionary[token.lemma_] += 1

            if token.text not in tokensDictionary:
                tokensDictionary[token.text] = 1
            else:
                tokensDictionary[token.text] += 1

    #Calculating number of sentences
    currentSentence = 0
    data = corpus[i]
    doc = nlp(data)
    while currentSentence < len(doc):
        if str(doc[currentSentence].sent[0]) != "\n": #This if is not needed, but it is a reminder for further processing
            numberOfSentences += 1                    # that some senteneces start with \n
        elif str(doc[currentSentence].sent) != "\n":
            numberOfSentences += 1
        currentSentence += len(doc[currentSentence].sent)
    i+=1

del tokensDictionary['nikusor']
del tokensDictionary['29.97']
del lemmasDictionary['nikusor']
del lemmasDictionary['29.97']

sortedTokensDictionary = {k: v for k, v in sorted(tokensDictionary.items(), key=lambda item: item[1], reverse=True)}
numberOfWords = 0

for currentWordNumber in tokensDictionary.values():
    numberOfWords += currentWordNumber

print("The number of unique words is: ", len(tokensDictionary))
print("The total number of words is: ", numberOfWords)
print("The total number of lemmas is: ", len(lemmasDictionary))
print("The total number of sentences is: ", numberOfSentences)
print("List of words ordered by frequency")
#print(sortedTokensDictionary)
for k, v in sortedTokensDictionary.items():
    print(k, end=': ')
    print(v)
