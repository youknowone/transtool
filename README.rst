transtool
=========
transtool is dictionary-rewritting-base general-purpose translation copilier.

Example
-------
An example under directory `bin`

Command::

    cd && bin
    ./transkorean input.txt


Input (input.txt)::

    여러 해 동안 모아 온 다양한 {{tip}}, {{trick}}, {{pattern}}, {{code}} {{snippet}}, {{technique을}} 소개합니다.
    잠깐, {{dict: value}, {dict: value}} 같은 {{python:dictionary은}} 예외입니다.

Output::

    여러 해 동안 모아 온 다양한 팁, 트릭, 패턴, 코드 스니펫, 테크닉을 소개합니다.
    잠깐, {{dict: value}, {dict: value}} 같은 딕셔너리는 예외입니다.

Dictionary (dictionary.ini)::

    [python]
    list=리스트
    tuple=튜플
    class=클래스
    object=객체
    function=함수
    method=메소드
    value=값
    dictionary=딕셔너리
    [web]
    web=웹
    browser=브라우저
    hypertext=하이퍼텍스트
    form=폼
    [general]
    form=형식
    tip=팁
    trick=트릭
    pattern=패턴
    code=코드
    snippet=스니펫
    technique=테크닉
