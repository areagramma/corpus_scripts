""" A file which provides the statistics for words
"""


def get_lemmas(self, token):
    """ Calculates the number of appearances of a lemma
    """
    self.lemmas[token.lemma_] += 1


def get_words(self, token):
    """ Calculates the number of appearances of a word
    """
    self.words[token.text] += 1


def get_word_len_chars(self, token):
    """ Calculates the number of appearances of a word based on it's length in characters
    """
    self.wordLensChars[str(len(token.text))] += 1


def get_syllables(self, token):
    """ Splits the word in syllables and returns it as a list
    """
    syllables = self.myPyphen.inserted(token.text).split('-')  # Divide the token in syllables and split it
    return syllables


def get_word_len_syl(self, token):
    """ Calculates the number of appearances of a word based on it's length in syllables
    """
    syllables = get_syllables(self, token)
    self.wordsLensSyl[str(len(syllables))] += 1
