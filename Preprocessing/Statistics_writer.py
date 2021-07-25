""" This file is for writing all the statistics generated. The words statistics will be written in "Words_statistics"
and the sentences statistics will be written in "Sentences_statistics".
"""
import os


def write_statistics(self):
    dir_path = os.path.dirname(os.path.realpath(__file__))  # Get the directory from which the code runs
    for currentWordAppearances in self.words.values():
        self.numberOfWords += currentWordAppearances

    stringToWrite = "The total number of words is " + str(self.numberOfWords) + "\n"
    stringToWrite += "The number of unique words is " + str(len(self.words)) + "\n"
    stringToWrite += "The total number of lemmas is " + str(len(self.lemmas)) + "\n"
    stringToWrite += "The total number of entities is " + str(self.numberOfEntities) + "\n"

    stringToWrite += "------------------------------------------------------------------------------------\n"
    stringToWrite += "Words lengths in chars: " + "\n"
    self.wordLensChars = {k: v for k, v in
                          sorted(self.wordLensChars.items(), key=lambda item: item[1], reverse=True)}
    for k, v in self.wordLensChars.items():
        stringToWrite += str(k) + " characters: " + str(v) + "\n"

    stringToWrite += "------------------------------------------------------------------------------------\n"
    stringToWrite += "Words lengths in syllables: " + "\n"
    self.wordsLensSyl = {k: v for k, v in
                         sorted(self.wordsLensSyl.items(), key=lambda item: item[1], reverse=True)}
    for k, v in self.wordsLensSyl.items():
        stringToWrite += str(k) + " syllables: " + str(v) + "\n"

    stringToWrite += "------------------------------------------------------------------------------------\n"
    stringToWrite += "List of words ordered by frequency: " + "\n"
    self.words = {k: v for k, v in
                  sorted(self.words.items(), key=lambda item: item[1], reverse=True)}
    for k, v in self.words.items():
        stringToWrite += str(k) + ": " + str(v) + "\n"

    output = open(dir_path + "\\" + "Words_statistics.txt", "w", encoding="utf8")  # This includes number of words,
    # unique words, lemmas, entities, words lengths in chars and syllables and a list of words ordered by frequency
    output.write(stringToWrite)
    output.close()

    stringToWrite = "The total number of sentences is " + str(self.numberOfSentences) + "\n"
    stringToWrite += "Entities per sentence: " + "\n"
    self.entsPerSent = {k: v for k, v in
                        sorted(self.entsPerSent.items(), key=lambda item: item[1], reverse=True)}
    for k, v in self.entsPerSent.items():
        stringToWrite += str(k) + " entities: " + str(v) + "\n"

    stringToWrite += "------------------------------------------------------------------------------------\n"
    stringToWrite += "Sentences lengths: " + "\n"
    self.sentLens = {k: v for k, v in
                     sorted(self.sentLens.items(), key=lambda item: item[1], reverse=True)}
    for k, v in self.sentLens.items():
        stringToWrite += str(k) + " words: " + str(v) + "\n"

    output = open(dir_path + "\\" + "Sentences_statistics.txt", "w", encoding="utf8")  # This includes
    # number of sentences, entities per sentence and sentences lengths
    output.write(stringToWrite)
    output.close()
