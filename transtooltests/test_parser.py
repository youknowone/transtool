
# -*- coding: utf-8 -*-
from transtool.parser import PythonParser

sentence = u'''여러 해 동안 모아 온 다양한 {{tip}}, {{trick}}, {{pattern}}, {{code}} {{snippet}}, {{technique을}} 소개합니다.
잠깐, {{dict: value}, {dict: value}} 같은 {{python:dictionary는}} 예외입니다.
'''
def test_parser():
    parser = PythonParser(sentence)
    assert parser
    assert parser.next() == (u'여러 해 동안 모아 온 다양한 ', u'tip')
    assert parser.next() == (u', ', u'trick')
    assert parser.next() == (u', ', u'pattern')
    assert parser.next() == (u', ', u'code')
    assert parser.next() == (u' ', u'snippet')
    assert parser.next() == (u', ', u'technique을')
    prepart, word = parser.next()
    assert prepart == u' 소개합니다.\n잠깐, {{dict: value}, {dict: value}} 같은 '
    assert word == u'python:dictionary는'
    assert word.tag == u'python'
    assert word.expression == u'dictionary는'
    assert parser.next() == (u' 예외입니다.\n', None)