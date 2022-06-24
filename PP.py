import re
import string


class Preprocess:
    def __init__(self, data, lower=False, rm_punctuation=False, rm_digits=False, tokenize=False, tfidf=False):
        self.data = data
        self.lower = lower
        self.rm_punctuation = rm_punctuation
        self.rm_digits = rm_digits
        self.tokenize = tokenize
        self.tfidf = tfidf

        if self.lower:
            self.data = self.make_lower()

        if rm_punctuation:
            self.data = self.remove_punctuation()

        if rm_digits:
            self.data = self.remove_digits()

        if tokenize:
            self.data = self.make_tokens()

        if self.tfidf:
            self.data = self.make_tfidf()

    def make_lower(self):
        return self.data.lower()

    def remove_punctuation(self):
        self.data = re.sub('[%s]' % re.escape(string.punctuation), '', self.data)
        return self.data

    def remove_digits(self):
        self.data = re.sub('W*dw*', '', self.data)
        return self.data

    def make_tokens(self):
        pass

    def make_tfidf(self):
        # TODO tfidf
        pass

    def __repr__(self):
        return self.data
