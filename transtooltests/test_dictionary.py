
#-*- coding: utf-8 -*-
from transtool.dictionary import INILoader
from transtool.dictionary.models import KoreanPackage
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
    return package

def test_korean_dictionary():
    l = INILoader('test.ini', Package=KoreanPackage)
    package = l.gen_package()
    package.build_index()

    assert package.get(u'list는').candidate == u'리스트는'
    assert package.get(u'list가').candidate == u'리스트가'
    assert package.get(u'list를').candidate == u'리스트를'
    assert package.get(u'tuple은').candidate == u'튜플은'
    assert package.get(u'tuple이').candidate == u'튜플이'
    assert package.get(u'tuple을').candidate == u'튜플을'
    assert package.get(u'list을').candidate == u'리스트를'
    assert package.get(u'tuple가').candidate == u'튜플이'
    assert package.get(u'dictionary는').candidate == u'딕셔너리는'

    return package

if __name__ == '__main__':
    test_dictionary()
