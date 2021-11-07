""" This file is for writing all the statistics generated. The words statistics will be written in "Words_statistics"
and the sentences statistics will be written in "Sentences_statistics".
"""
import os


def write_statistics(AGSModel):
    dir_path = os.path.dirname(os.path.realpath(__file__))  # Get the directory from which the code runs
    for currentWordAppearances in AGSModel.words.values():
        AGSModel.numberOfWords += currentWordAppearances

    stringToWrite = "The total number of words is " + str(AGSModel.numberOfWords) + "\n"
    stringToWrite += "The number of unique words is " + str(len(AGSModel.words)) + "\n"
    stringToWrite += "The total number of lemmas is " + str(len(AGSModel.lemmas)) + "\n"
    stringToWrite += "The total number of entities is " + str(AGSModel.numberOfEntities) + "\n"

    stringToWrite += "------------------------------------------------------------------------------------\n"
    stringToWrite += "Words lengths in chars: " + "\n"
    AGSModel.wordLensChars = {k: v for k, v in
                          sorted(AGSModel.wordLensChars.items(), key=lambda item: item[1], reverse=True)}
    for k, v in AGSModel.wordLensChars.items():
        stringToWrite += str(k) + " characters: " + str(v) + "\n"

    stringToWrite += "------------------------------------------------------------------------------------\n"
    stringToWrite += "Words lengths in syllables: " + "\n"
    AGSModel.wordsLensSyl = {k: v for k, v in
                         sorted(AGSModel.wordsLensSyl.items(), key=lambda item: item[1], reverse=True)}
    for k, v in AGSModel.wordsLensSyl.items():
        stringToWrite += str(k) + " syllables: " + str(v) + "\n"

    stringToWrite += "------------------------------------------------------------------------------------\n"
    stringToWrite += "List of words ordered by frequency: " + "\n"
    AGSModel.words = {k: v for k, v in
                  sorted(AGSModel.words.items(), key=lambda item: item[1], reverse=True)}
    for k, v in AGSModel.words.items():
        stringToWrite += str(k) + ": " + str(v) + "\n"

    output = open(dir_path + "\\" + "Words_statistics.txt", "w", encoding="utf8")  # This includes number of words,
    # unique words, lemmas, entities, words lengths in chars and syllables and a list of words ordered by frequency
    output.write(stringToWrite)
    output.close()

    stringToWrite = "The total number of sentences is " + str(AGSModel.numberOfSentences) + "\n"
    stringToWrite += "Entities per sentence: " + "\n"
    AGSModel.entsPerSent = {k: v for k, v in
                        sorted(AGSModel.entsPerSent.items(), key=lambda item: item[1], reverse=True)}
    for k, v in AGSModel.entsPerSent.items():
        stringToWrite += str(k) + " entities: " + str(v) + "\n"

    stringToWrite += "------------------------------------------------------------------------------------\n"
    stringToWrite += "Sentences lengths: " + "\n"
    AGSModel.sentLens = {k: v for k, v in
                     sorted(AGSModel.sentLens.items(), key=lambda item: item[1], reverse=True)}
    for k, v in AGSModel.sentLens.items():
        stringToWrite += str(k) + " words: " + str(v) + "\n"

    output = open(dir_path + "\\" + "Sentences_statistics.txt", "w", encoding="utf8")  # This includes
    # number of sentences, entities per sentence and sentences lengths
    output.write(stringToWrite)
    output.close()
