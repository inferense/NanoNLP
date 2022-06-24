import re


class RegexTokenizer:
    r"""
    A tokenizer that splits a string using a regular expression, which
    matches either the tokens or the separators between tokens.

        '>>> tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')'

    :type pattern: str
    :param pattern: The pattern used to build this tokenizer.
        (This pattern must not contain capturing parentheses;
        Use non-capturing parentheses, e.g. (?:...), instead)
    :type gaps: bool
    :param gaps: True if this tokenizer's pattern should be used
        to find separators between tokens; False if this
        tokenizer's pattern should be used to find the tokens
        themselves.
    :type discard_empty: bool
    :param discard_empty: True if any empty tokens `''`
        generated by the tokenizer should be discarded.  Empty
        tokens can only be generated if `_gaps == True`.
    :type flags: int
    :param flags: The regexp flags used to compile this
        tokenizer's pattern.  By default, the following flags are
        used: `re.UNICODE | re.MULTILINE | re.DOTALL`.

    """

    def __init__(
        self,
        pattern,
        gaps=False,
        discard_empty=True,
        flags=re.UNICODE | re.MULTILINE | re.DOTALL,
    ):
        # If they gave us a regexp object, extract the pattern.
        pattern = getattr(pattern, "pattern", pattern)

        self._pattern = pattern
        self._gaps = gaps
        self._discard_empty = discard_empty
        self._flags = flags
        self._regexp = None

    def _check_regexp(self):
        if self._regexp is None:
            self._regexp = re.compile(self._pattern, self._flags)

    def tokenize(self, text):
        self._check_regexp()
        # If our regexp matches gaps, use re.split:
        if self._gaps:
            if self._discard_empty:
                return [tok for tok in self._regexp.split(text) if tok]
            else:
                return self._regexp.split(text)

        # If our regexp matches tokens, use re.findall:
        else:
            return self._regexp.findall(text)

    def __repr__(self):
        return "{}(pattern={!r}, gaps={!r}, discard_empty={!r}, flags={!r})".format(
            self.__class__.__name__,
            self._pattern,
            self._gaps,
            self._discard_empty,
            self._flags,
        )


class WhitespaceTokenizer(RegexTokenizer):
    r"""
    Tokenize a string on whitespace (space, tab, newline).
    In general, users should use the string ``split()`` method instead.

        '>>> s = "Good muffins cost $3.88\nin New York.  Please buy me\ntwo of them.\n\nThanks."'
        '>>> WhitespaceTokenizer().tokenize(s)'
        ['Good', 'muffins', 'cost', '$3.88', 'in', 'New', 'York.',
        'Please', 'buy', 'me', 'two', 'of', 'them.', 'Thanks.']
    """

    def __init__(self):
        RegexTokenizer.__init__(self, r"\s+", gaps=True)


class BlanklineTokenizer(RegexTokenizer):
    """
    Tokenize a string, treating any sequence of blank lines as a delimiter.
    Blank lines are defined as lines containing no characters, except for
    space or tab characters.
    """

    def __init__(self):
        RegexTokenizer.__init__(self, r"\s*\n\s*\n\s*", gaps=True)


class WordPunctTokenizer(RegexTokenizer):
    r"""
    Tokenize a text into a sequence of alphabetic and
    non-alphabetic characters, using the regexp ``\w+|[^\w\s]+``.
        '>>> s = "Good muffins cost $3.88\nin New York.  Please buy me\ntwo of them.\n\nThanks."'
        '>>> WordPunctTokenizer().tokenize(s)'
        ['Good', 'muffins', 'cost', '$', '3', '.', '88', 'in', 'New', 'York',
        '.', 'Please', 'buy', 'me', 'two', 'of', 'them', '.', 'Thanks', '.']
    """

    def __init__(self):
        RegexTokenizer.__init__(self, r"\w+|[^\w\s]+")


######################################################################
# { Tokenization Functions
######################################################################

def regexp_tokenize(
    text,
    pattern,
    gaps=False,
    discard_empty=True,
    flags=re.UNICODE | re.MULTILINE | re.DOTALL,
):
    """
    Return a tokenized copy of *text*.  See :class:`.RegexpTokenizer`
    for descriptions of the arguments.
    """
    tokenizer = RegexTokenizer(pattern, gaps, discard_empty, flags)
    return tokenizer.tokenize(text)


blankline_tokenize = BlanklineTokenizer().tokenize
wordpunct_tokenize = WordPunctTokenizer().tokenize