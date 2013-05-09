
class Rewriter(object):
    def __init__(self, wordpack, Parser):
        self.wordpack = wordpack
        self.Parser = Parser

    def resolve(self, text):
        parser = self.Parser(text)
        parts = []
        for sentence, token in parser:
            parts.append(sentence)
            if token is not None:
                rewritten = self.wordpack.get(token.expression, token.tag)
                expression = self.resolve(rewritten.candidate)
                parts.append(expression)
        return u''.join(parts)

