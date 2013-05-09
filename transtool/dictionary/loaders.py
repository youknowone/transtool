
import ConfigParser
from models import Package, Dictionary, Word

class INILoader(object):
    def __init__(self, filename, charset='utf-8', Word=Word, Dictionary=Dictionary, Package=Package):
        self.parser = ConfigParser.ConfigParser()
        self.parser.read(filename)
        self.charset = charset
        self.Word, self.Dictionary, self.Package = Word, Dictionary, Package

    def gen_dicts(self):
        for section in self.parser.sections():
            dictionary = self.Dictionary(section.decode(self.charset))
            for key, val in self.parser.items(section):
                ukey, uval = key.decode(self.charset), val.decode(self.charset)
                word = self.Word(ukey, uval)
                dictionary.add_word(word)
            yield dictionary

    def gen_package(self):
        pack = self.Package()
        for dic in self.gen_dicts():
            pack.add_dictionary(dic)
        return pack
