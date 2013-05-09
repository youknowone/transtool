
class Word(unicode):
    def __init__(self, string):
        super(Word, self).__init__(string)
        if not u':' in string:
            self.tag, self.expression = None, string
        else:
            self.tag, self.expression = string.split(u':', 1)
        self.__length__ = len(string)

