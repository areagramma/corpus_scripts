""" Area Gramma statistics
Be sure to install spacy with your desired language using "python -m spacy download *spacy_model*"
(for more information go to https://spacy.io/models). For spacy documentation go to
https://spacy.io/usage/spacy-101. Other useful links for spacy are https://spacy.io/api/token#attributes &&
https://universaldependencies.org/docs/u/pos/
For pyphen (used for syllables) check https://pyphen.org/
"""
import Words_statistics_generator as WSG
import Sentences_statistics_generator as SSG
import Statistics_writer as SW
from collections import defaultdict


class AGStatistics:
    """ Area Gramma statistics generator
    This class uses spacy models and pyphen to generate statistics based on the given data. It generates 3 statistics
    for sentences and 7 statistics for words. More information will be provided for each function. If provided a big
    corpus, the process will take a lot of time.
    """
    corpus = []  # The corpus for which we will get the statistics
    showProgress = True  # Displays a progress of the process
    # Words statistics
    lemmas = defaultdict(int)  # Lemmas
    words = defaultdict(int)  # Words
    punctuations = defaultdict(int)  # Punctuations (not used anywhere at the moment)
    wordLensChars = defaultdict(int)  # Words lengths in chars
    wordsLensSyl = defaultdict(int)  # Words lengths in syllables
    numberOfEntities = 0  # Total number of entities in the corpus (generated in get_entities_in_sentence(sentence))
    numberOfWords = 0  # Total number of words in the corpus
    # Sentences statistics
    sentLens = defaultdict(int)  # Sentences lengths
    entsPerSent = defaultdict(int)  # Number of entities per sentence
    numberOfSentences = 0  # Total number of sentences in the corpus

    # Initialization of the corpus (please provide a list of strings)
    def __init__(self, corpus, nlpModel, pyphenModel, showCurrentPosition=True):
        self.corpus = corpus
        self.showProgress = showCurrentPosition  # If set to 'False', no progress will be shown
        self.nlp = nlpModel  # The spacy model which will be used
        self.pyphen = pyphenModel  # The pyphen model which will be used

    # Generate all statistics in output files
    def generate_statistics(self):
        """ Takes every text provided and calls all the other functions to generate the statistics listed above
        """
        data = list(self.nlp.pipe(self.corpus, batch_size=100))
        i = 1
        for doc in data:
            if self.showProgress:
                print("Current progress: " + str(i) + " out of " + str(len(self.corpus)) + " texts completed")
                i += 1
            SSG.get_sentence_statistics(self, doc)
            for token in doc:
                if token.pos_ == 'PUNCT' or token.text == '\n':
                    if token.text not in self.punctuations:
                        self.punctuations[token.text] = 1
                    else:
                        self.punctuations[token.text] += 1
                else:
                    WSG.get_words_statistics(self, token)
        SW.write_statistics(self)
        print("All done")
