
class BaseParser(object):
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        while True:
            item = self.next()
            if item is None:
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
        while True:
            if not opened:
                if not match(self.__opener__):
                    self.index += 1
                    continue
                opened = True
                self.index += len(self.__opener__)
                start = self.index
            if opened:
                if match(self.__blacklist__):
                    opened = False
                    start = None
                    continue
                if not match(self.__closer__):
                    self.index += 1
                    continue
                word = self.data[start:self.index]
                self.index += len(self.__closer__)
                return word

