
#-*- coding: utf-8 -*-
from transtool.dictionary import INILoader
from transtool.dictionary.exc import WordNotFound, MultipleCandidates

def assertlog(cond, *logitems):
    try:
        assert cond
    except AssertionError as e:
        if logitems:
            for item in logitems:
                print item,
            print ''

def test_dictionary():
    l = INILoader('test.ini')
    package = l.gen_package()
    package.build_index()
    w = package.get('list')

    assertlog(package.get('list').candidate == u'리스트', package.get('list'), u'리스트')
    assert package.get('tuple').candidate == u'튜플'
    assert package.get('list', 'python').candidate == u'리스트'

    try:
        package.get('list', 'web')
    except WordNotFound:
        pass

    try:
        package.get('form')
    except MultipleCandidates:
        pass

if __name__ == '__main__':
    test_dictionary()
