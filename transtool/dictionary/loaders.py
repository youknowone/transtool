
import ConfigParser
from models import Package, Dictionary, Word

class INILoader(object):
    def __init__(self, filename, charset='utf-8'):
        self.parser = ConfigParser.ConfigParser()
        self.parser.read(filename)
        self.charset = charset

    def gen_dicts(self):
        for section in self.parser.sections():
            dictionary = Dictionary(section.decode(self.charset))
            for key, val in self.parser.items(section):
                ukey, uval = key.decode(self.charset), val.decode(self.charset)
                word = Word(ukey, uval)
                dictionary.add_word(word)
            yield dictionary

    def gen_package(self):
        pack = Package()
        for dic in self.gen_dicts():
            pack.add_dictionary(dic)
        return pack
