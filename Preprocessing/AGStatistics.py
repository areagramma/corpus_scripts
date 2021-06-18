# Area Gramma statistics
import spacy  # Be sure to install it  with "python -m spacy download ro_core_news_lg" (for more information
# go to https://spacy.io/models/ro). For spacy documentation go to https://spacy.io/usage/spacy-101. Other useful
# links for spacy are https://spacy.io/api/token#attributes && https://universaldependencies.org/docs/u/pos/
import pyphen  # Used for syllables (https://pyphen.org/)
import os


class AGStatistics:
    corpus = []  # The corpus for which we will get the statistics
    nlp = spacy.load("ro_core_news_lg")
    myPyphen = pyphen.Pyphen(lang='ro')
    # A lot of the statistics are represented by dictionaries
    lemmas = dict()  # Lemmas
    words = dict()  # Words
    punctuations = dict()  # Punctuations (maybe not needed?)
    avgWordLenChars = dict()  # Average word length in chars
    avgWordLenSyl = dict()  # Average word length in syllables
    avgSentLen = dict()  # Average sentence length
    avgEntPerSent = dict()  # Average number of entities per sentence
    numberOfSentences = 0  # Total number of sentences in the corpus
    numberOfEntities = 0  # Total number of entities in the corpus (generated in get_entities_in_sentence(sentence))
    numberOfWords = 0  # Total number of words in the corpus
    showProgress = False

    # Initialization of the corpus (please provide a list of strings)
    def __init__(self, corpus, showProgress=False):
        self.corpus = corpus
        self.showProgress = showProgress

    def get_lemmas(self, token):
        if token.lemma_ not in self.lemmas:
            self.lemmas[token.lemma_] = 1
        else:
            self.lemmas[token.lemma_] += 1

    def get_words(self, token):
        if token.text not in self.words:
            self.words[token.text] = 1
        else:
            self.words[token.text] += 1

    def get_word_len_chars(self, token):
        if str(len(token.text)) not in self.avgWordLenChars:
            self.avgWordLenChars[str(len(token.text))] = 1
        else:
            self.avgWordLenChars[str(len(token.text))] += 1

    def get_word_len_syl(self, token):
        syllables = self.myPyphen.inserted(token.text).split('-')  # Divide the token in syllables and split it
        if str(len(syllables)) not in self.avgWordLenSyl:
            self.avgWordLenSyl[str(len(syllables))] = 1
        else:
            self.avgWordLenSyl[str(len(syllables))] += 1

    def get_sentence_statistics(self, doc):
        currentWordNumber = 0  # The number of the current word in the doc

        def get_sentence_length(sentence):
            if str(len(sentence)) not in self.avgSentLen:
                self.avgSentLen[str(len(sentence))] = 1
            else:
                self.avgSentLen[str(len(sentence))] += 1

        def get_entities_in_sentence(sentence):
            numberEnts = 0  # The number of entities in the current sentence
            for currentWord in sentence:
                if currentWord.pos_ == 'PROPN':
                    numberEnts += 1
                    self.numberOfEntities += 1  # The total number of entities in the corpus
            if str(numberEnts) not in self.avgEntPerSent:
                self.avgEntPerSent[str(numberEnts)] = 1
            else:
                self.avgEntPerSent[str(numberEnts)] += 1

        while currentWordNumber < len(doc):
            currentSentence = doc[currentWordNumber].sent  # Get the sentence for which the current word belongs
            if str(currentSentence) != "\n":
                self.numberOfSentences += 1
                get_sentence_length(currentSentence)
                get_entities_in_sentence(currentSentence)
            currentWordNumber += len(doc[currentWordNumber].sent)

    def write_statistics(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))  # Get the directory from which the code runs
        for currentWordNumber in self.words.values():
            self.numberOfWords += currentWordNumber

        stringToWrite = "The total number of words is " + str(self.numberOfWords) + "\n"
        stringToWrite += "The number of unique words is " + str(len(self.words)) + "\n"
        stringToWrite += "The total number of lemmas is " + str(len(self.lemmas)) + "\n"
        stringToWrite += "The total number of entities is " + str(self.numberOfEntities) + "\n"

        stringToWrite += "------------------------------------------------------------------------------------\n"
        stringToWrite += "Average word length in chars: " + "\n"
        self.avgWordLenChars = {k: v for k, v in
                                sorted(self.avgWordLenChars.items(), key=lambda item: item[1], reverse=True)}
        for k, v in self.avgWordLenChars.items():
            stringToWrite += str(k) + " characters: " + str(v) + "\n"

        stringToWrite += "------------------------------------------------------------------------------------\n"
        stringToWrite += "Average word length in syllables: " + "\n"
        self.avgWordLenSyl = {k: v for k, v in
                              sorted(self.avgWordLenSyl.items(), key=lambda item: item[1], reverse=True)}
        for k, v in self.avgWordLenSyl.items():
            stringToWrite += str(k) + " syllables: " + str(v) + "\n"

        stringToWrite += "------------------------------------------------------------------------------------\n"
        stringToWrite += "List of words ordered by frequency: " + "\n"
        self.words = {k: v for k, v in
                      sorted(self.words.items(), key=lambda item: item[1], reverse=True)}
        for k, v in self.words.items():
            stringToWrite += str(k) + ": " + str(v) + "\n"

        output = open(dir_path + "\\" + "Words_statistics.txt", "w", encoding="utf8")  # This includes number of words,
        # unique words, lemmas, average word, length and entities
        output.write(stringToWrite)
        output.close()

        stringToWrite = "The total number of sentences is " + str(self.numberOfSentences) + "\n"
        stringToWrite += "Average entities per sentence: " + "\n"
        self.avgEntPerSent = {k: v for k, v in
                              sorted(self.avgEntPerSent.items(), key=lambda item: item[1], reverse=True)}
        for k, v in self.avgEntPerSent.items():
            stringToWrite += str(k) + " entities: " + str(v) + "\n"

        stringToWrite += "------------------------------------------------------------------------------------\n"
        stringToWrite += "Average sentence length: " + "\n"
        self.avgSentLen = {k: v for k, v in
                           sorted(self.avgSentLen.items(), key=lambda item: item[1], reverse=True)}
        for k, v in self.avgSentLen.items():
            stringToWrite += str(k) + " words: " + str(v) + "\n"

        output = open(dir_path + "\\" + "Sentences_statistics.txt", "w", encoding="utf8")  # This includes
        # number of sentences, entities per sentence and sentence length
        output.write(stringToWrite)
        output.close()

    # Generate all statistics in output files
    def generate_statistics(self):
        i = 0
        for data in self.corpus:
            if self.showProgress:
                print("Current progress: " + str(i) + " out of " + str(len(self.corpus)) + " texts completed")
                i += 1
            doc = self.nlp(data)
            self.get_sentence_statistics(doc)
            doc = self.nlp(data.lower())
            for token in doc:
                if token.pos_ == 'PUNCT' or token.text == '\n':
                    if token.text not in self.punctuations:
                        self.punctuations[token.text] = 1
                    else:
                        self.punctuations[token.text] += 1
                else:
                    self.get_lemmas(token)
                    self.get_words(token)
                    self.get_word_len_chars(token)
                    self.get_word_len_syl(token)
        self.write_statistics()
