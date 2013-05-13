
# -*- coding: utf-8 -*-
from . import exc

class Word(object):
    def __init__(self, source, candidate, tag=None):
        self.source = source
        self.candidate = candidate
        self.tag = tag
        assert unicode == type(self.source) == type(self.candidate)

    def __repr__(self):
        return u'<Word:{tag}:{source}=>{candidate}>'.format(tag=self.tag if self.tag else u'', source=self.source, candidate=self.candidate)

    def copy(self, source=False, candidate=False, tag=False):
        nsource = source if source is not False else self.source
        ncandidate = candidate if candidate is not False else self.candidate
        ntag = tag if tag is not False else self.tag
        return Word(nsource, ncandidate, ntag)


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

korean_makers = [
    (u'은', u'는'),
    (u'이', u'가'),
    (u'을', u'를'),
    (u'과', u'와'),
    (u'으로', u'로'),
    (u'나', u'이나'),
    (u'해'),
    (u'되'),
    (u'합'),
    (u'됩'),
]

class KoreanPackage(Package):
    def add_index(self, word, tag=None):
        super(KoreanPackage, self).add_index(word, tag)
        self.linearpool.append((word, tag))

    def build_index(self):
        i_ga = ord(u'가')
        i_hih = ord(u'힣')
        self.linearpool = []
        super(KoreanPackage, self).build_index()
        pool = self.linearpool[:]
        for word, tag in pool:
            if len(word.candidate) == 0:
                continue
            charval = ord(word.candidate[-1])
            if not (i_ga <= charval <= i_hih):
                continue
            jongval = (charval - i_ga) % 28
            for makers in korean_makers:
                maker = makers[0] if len(makers) == 1 else makers[0] if jongval else makers[1]
                for dmaker in makers:
                    kword = word.copy(source=word.source + dmaker,
                                      candidate=word.candidate + maker)
                    if kword.source not in self.word_index and\
                            (tag is None or kword.source not in self.tag_index[tag]):
                        self.add_index(kword, tag)
