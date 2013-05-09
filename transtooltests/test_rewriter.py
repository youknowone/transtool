
#-*- coding: utf-8 -*-
from transtool.rewriter import Rewriter
from transtool.parser import PythonParser

from test_parser import sentence
from test_dictionary import test_dictionary

def test_rewriter():
    wordpack = test_dictionary()
    rewriter = Rewriter(wordpack, PythonParser)

    resolved = rewriter.resolve(sentence)
    print resolved
    assert resolved == u'여러 해 동안 모아 온 다양한 팁, 트릭, 패턴, 코드 스니펫, 테크닉을 소개합니다.\n잠깐, {{dict: value}, {dict: value}} 같은 딕셔너리는 예외입니다.\n'
