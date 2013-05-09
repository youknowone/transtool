
class Word(unicode):
    def __init__(self, string):
        unicode.__init__(self, string)
        if not u':' in string:
            self.category = None
            self.expression = string
            self.tag = None
        else:
            self.category, other = string.split(u':', 1)
            if u':' in other:
                self.tag, self.expression = string.split(u':', 1)
            else:
                self.tag = None
                self.expression = other
