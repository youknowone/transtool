
# -*- coding: utf-8 -*-
from transtool.parser import PythonParser

def test_parser():
    sentence = u'''여러 해 동안 모아 온 다양한 {{tip}}, {{trick}}, {{pattern}}, {{code}} {{snippet}}, {{technique을}} 소개합니다.
잠깐, {{dict: value}, {dict: value}} 같은 {{python:dictionary는}} 예외입니다.
'''
    parser = PythonParser(sentence)
    assert parser
    assert parser.next() == u'tip'
    assert parser.next() == u'trick'
    assert parser.next() == u'pattern'
    assert parser.next() == u'code'
    assert parser.next() == u'snippet'
    assert parser.next() == u'technique을'
    word = parser.next()
    assert word == u'python:dictionary는'
    assert word.category == u'python'
    assert word.expression == u'dictionary는'