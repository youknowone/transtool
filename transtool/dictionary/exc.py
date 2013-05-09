
from prettyexc import PrettyException as Exception

class DictionaryException(Exception): pass
class WordNotFound(DictionaryException): pass
class MultipleCandidates(DictionaryException): pass
