""" A file which provides the statistics for sentences
"""


def get_sentence_length(AGSModel, sentence):
    """ Calculates the number of appearances of sentences based on it's number of words
    """
    AGSModel.sentLens[str(len(sentence))] += 1


def get_entities_in_sentence(AGSModel, sentence):
    """ Calculates the number of appearances of sentences based on it's number of entities
    """
    numberEnts = len(sentence.ents)  # The number of entities in the current sentence
    AGSModel.numberOfEntities += len(sentence.ents)  # The total number of entities in the corpus
    AGSModel.entsPerSent[str(numberEnts)] += 1


def get_sentence_statistics(AGSModel, doc):
    """ Generates the above statistics and calculates the total number of sentences
    """
    currentWordNumber = 0  # The number of the current word in the doc
    while currentWordNumber < len(doc):
        currentSentence = doc[currentWordNumber].sent  # Get the sentence for which the current word belongs
        if str(currentSentence) != "\n":
            AGSModel.numberOfSentences += 1
            get_sentence_length(AGSModel, currentSentence)
            get_entities_in_sentence(AGSModel, currentSentence)
        currentWordNumber += len(doc[currentWordNumber].sent)
