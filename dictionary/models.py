
class DictionaryException(Exception): pass
class WordNotFound(DictionaryException): pass
class MultipleCandidates(DictionaryException): pass

class Word(object):
    def __init__(self, source, candidate, tag=None):
        self.source = source
        self.candidate = candidate
        self.tag = tag

    def __repr__(self):
        return '<Word:{tag}:{source}=>{candidate}>'.format(tag=self.tag if self.tag else '', source=self.source, candidate=self.candidate.encode('utf-8'))

class Dictionary(object):
    def __init__(self, tag=None):
        self.tag = tag
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def __repr__(self):
        l = map(lambda w: w.__repr__(), self.words)
        return '<Dictionary:[' + u','.join(l) + u']>'

class Package(object):
    def __init__(self):
        self.dictionaries = []
        self.words = []
        self.tag_index = {}
        self.word_index = {}

    def add_dictionary(self, item):
        self.dictionaries.append(item)

    def add_word(self, item):
        self.words.append(item)

    def add_index(self, word, tag=None):
        def put(set, word):
            if word.source in set:
                set[word.source] = False
            else:
                set[word.source] = word
        if tag is not None:
            if not tag in self.tag_index:
                self.tag_index[tag] = {}
            put(self.tag_index[tag], word)
        put(self.word_index, word)    

    def build_index(self):
        for dictionary in self.dictionaries:
            for word in dictionary.words:
                self.add_index(word, dictionary.tag)
        for word in self.words:
            self.add_index(word)

    def get(self, source, tag=None):
        try:
            if tag is not None:
                result = self.tag_index[tag][source]
            result = self.word_index[source]
        except KeyError:
            raise WordNotFound()
        if not result:
            raise MultipleCandidates()
        return result