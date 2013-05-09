
from .word import Word

class BaseParser(object):
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.lastindex = 0

    def __iter__(self):
        while True:
            item = self.next()
            if item[1] is None:
                if len(item[0]) > 0:
                    yield item
                break
            yield item

class PythonParser(BaseParser):
    __opener__ = u'{{'
    __closer__ = u'}}'
    __blacklist__ = u','

    def next(self):
        def match(word):
            if self.data[self.index] != word[0]:
                return False
            if self.data[self.index:self.index + len(word)] != word:
                return False
            return True

        opened = False
        start = None
        while self.index < len(self.data):
            if not opened:
                if not match(self.__opener__):
                    self.index += 1
                    continue
                opened = True
                start = self.index
                self.index += len(self.__opener__)
            if opened:
                if match(self.__blacklist__):
                    opened = False
                    start = None
                    continue
                if not match(self.__closer__):
                    self.index += 1
                    continue
                sentence = self.data[self.lastindex:start]
                start += len(self.__opener__)
                word = self.data[start:self.index]
                self.index += len(self.__closer__)
                self.lastindex = self.index
                return sentence, Word(word)
        else:
            return self.data[self.lastindex:], None
