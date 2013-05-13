
from .dictionary import exc

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
                try:
                    rewritten = self.wordpack.get(token.expression.lower(), token.tag)
                except exc.WordNotFound:
                    print token, 'after:', sentence, token
                    raise
                expression = self.resolve(rewritten.candidate)
                parts.append(expression)
        return u''.join(parts)

