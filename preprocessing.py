import re
import string


def lower(text):
    return text.lower()


def rm_punctuation(text):
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    return text


def rm_digits(text):
    text = re.sub('W*dw*', '', text)
    return text


def tokenizer(text):
    #TODO tokenizer https://www.nltk.org/_modules/nltk/tokenize/regexp.html
    pass


def tfidf(text):
    # TODO tfidf
    pass

