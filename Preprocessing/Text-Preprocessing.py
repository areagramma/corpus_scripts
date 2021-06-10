#Read all the data
import os
os.chdir("E:\Area Gramma\Corpus\Spacy\Subs") #The folder containing the subs
files = os.listdir() #Get all the names of the files

inputPath = "E:\Area Gramma\Corpus\Spacy\Subs"

corpus = []
for file in files:
    fin = open(inputPath+'\\'+file, "rt", encoding="utf8")
    data = fin.read()
    corpus.append(data)
    fin.close()
print(len(corpus))




#Preprocessing && statistics
import spacy
import pyphen

lemmasDictionary = dict()
tokensDictionary = dict()
punctuationsDictionary = dict()
nlp = spacy.load("ro_core_news_lg")

i = 0
numberOfSentences = 0
numberOfEntities = 0
avgWordLenChars = dict()
avgSentenceLen = dict()
avgEntsPerSent = dict()
myPyphen = pyphen.Pyphen(lang='ro')
avgWordLenSyl = dict()
while i < 50:
    data = corpus[i]
    doc = nlp(data)
    for token in doc:
        if token.pos_ == 'PROPN':
            numberOfEntities += 1
        if str(len(myPyphen.inserted(token.text).split('-'))) not in avgWordLenSyl:
            avgWordLenSyl[str(len(myPyphen.inserted(token.text).split('-')))] = 1
        else:
            avgWordLenSyl[str(len(myPyphen.inserted(token.text).split('-')))] += 1

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
            if str(len(token.text)) not in avgWordLenChars:
                avgWordLenChars[str(len(token.text))] = 1
            else:
                avgWordLenChars[str(len(token.text))] += 1


    #Calculating number of sentences
    currentSentence = 0
    data = corpus[i]
    doc = nlp(data)
    while currentSentence < len(doc):
       # if str(doc[currentSentence].sent[0]) != "\n": #Just a reminder for further processing that some senteneces start with \n
         #   numberOfSentences += 1
        if str(doc[currentSentence].sent) != "\n":
            numberOfSentences += 1
        if str(len(doc[currentSentence].sent)) not in avgSentenceLen:
            avgSentenceLen[str(len(doc[currentSentence].sent))] = 1
        else:
            avgSentenceLen[str(len(doc[currentSentence].sent))] += 1
        currentWord = currentSentence
        entsInSent = 0

        while currentWord < (currentSentence + len(doc[currentSentence].sent)):
            if doc[currentWord].pos_ == 'PROPN':
                entsInSent += 1
            currentWord += 1
        if str(entsInSent) not in avgEntsPerSent:
            avgEntsPerSent[str(entsInSent)] = 1
        else:
            avgEntsPerSent[str(entsInSent)] += 1
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
print("The total number of entities is: ", numberOfEntities)
print("List of words ordered by frequency")
#print(sortedTokensDictionary)
for k, v in sortedTokensDictionary.items():
    print(k, end=': ')
    print(v)


avgWordLenChars = {k: v for k, v in sorted(avgWordLenChars.items(), key=lambda item: item[1], reverse=True)}
print("Average word length in characters: ")
for k, v in avgWordLenChars.items():
    print(k, end=' characters: ')
    print(v)

print("Average word length in syllables: ")
avgWordLenSyl = {k: v for k, v in sorted(avgWordLenSyl.items(), key=lambda item: item[1], reverse=True)}
for k, v in avgWordLenSyl.items():
    print(k, end=' syllables: ')
    print(v)

print("Average sentence length: ")
avgSentenceLen = {k: v for k, v in sorted(avgSentenceLen.items(), key=lambda item: item[1], reverse=True)}
for k, v in avgSentenceLen.items():
    print(k, end=' words: ')
    print(v)

print("Average entities per sentence: ")
avgEntsPerSent = {k: v for k, v in sorted(avgEntsPerSent.items(), key=lambda item: item[1], reverse=True)}
for k, v in avgEntsPerSent.items():
    print(k, end=' entities: ')
    print(v)

