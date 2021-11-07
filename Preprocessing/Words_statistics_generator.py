""" A file which provides the statistics for words
"""

def get_words_statistics(AGSModel, token):
    """ Generates all the statistics related to words
    """
    get_lemmas(AGSModel, token)
    get_words(AGSModel, token)
    get_word_len_chars(AGSModel, token)
    get_word_len_syl(AGSModel, token)

def get_lemmas(AGSModel, token):
    """ Calculates the number of appearances of a lemma
    """
    AGSModel.lemmas[token.lemma_] += 1


def get_words(AGSModel, token):
    """ Calculates the number of appearances of a word
    """
    AGSModel.words[token.text] += 1


def get_word_len_chars(AGSModel, token):
    """ Calculates the number of appearances of a word based on it's length in characters
    """
    AGSModel.wordLensChars[str(len(token.text))] += 1


def get_syllables(AGSModel, token):
    """ Splits the word in syllables and returns it as a list
    """
    syllables = AGSModel.pyphen.inserted(token.text).split('-')  # Divide the token in syllables and split it
    return syllables


def get_word_len_syl(AGSModel, token):
    """ Calculates the number of appearances of a word based on it's length in syllables
    """
    syllables = get_syllables(AGSModel, token)
    AGSModel.wordsLensSyl[str(len(syllables))] += 1
