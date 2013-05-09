
from . import exc

class Word(object):
    def __init__(self, source, candidate, tag=None):
        self.source = source
        self.candidate = candidate
        self.tag = tag
        assert unicode == type(self.source) == type(self.candidate)

    def __repr__(self):
        return u'<Word:{tag}:{source}=>{candidate}>'.format(tag=self.tag if self.tag else u'', source=self.source, candidate=self.candidate)


class Dictionary(object):
    def __init__(self, tag=None):
        self.tag = tag
        self.words = []

    def __repr__(self):
        l = [word.__repr__() for word  in self.words]
        return u'<Dictionary:[{}]>'.format(u','.join(l))

    def add_word(self, word):
        self.words.append(word)


class Package(object):
    def __init__(self):
        self.dictionaries = []
        self.words = []
        self.tag_index = {}
        self.word_index = {}

    def __repr__(self):
        return u'<Package(dictionaries={})>'.format(self.dictionaries)

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
            else:
                result = self.word_index[source]
        except KeyError:
            raise exc.WordNotFound(source=source)
        if not result:
            raise exc.MultipleCandidates(source=source)
        return result