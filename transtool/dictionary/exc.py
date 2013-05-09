
class DictionaryException(Exception): pass
class WordNotFound(DictionaryException): pass
class MultipleCandidates(DictionaryException): pass
