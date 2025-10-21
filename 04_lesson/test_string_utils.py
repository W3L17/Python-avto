import pytest
from string_utils import StringUtils


#Позитивные сценария 

@pytest.mark.parametrize("input_word,expected",
[("привет","Привет"),
("тест","Тест"),
("python","Python"),
("line","Line"),
("中国","中国")
])
def test_capitalize_positive(input_word,expected):
    stringUtils = StringUtils()
    res = stringUtils.capitalize(input_word)
    assert res == expected


@pytest.mark.parametrize("input_word,expected",
[("  Good","Good"),
("   Sky","Sky"),
("",""),
("Good  ","Good  "),
("Sky  ","Sky  ")

])
def test_trim_positive(input_word,expected):
    stringUtils = StringUtils()
    res = stringUtils.trim(input_word)
    assert res == expected



@pytest.mark.parametrize("string,symbol,expected",
[("Sky","S",True),
("Python","y",True),
("Jav6","6",True)
])
def test_contains_positive(string,symbol,expected):
    stringUtils = StringUtils()
    res = stringUtils.contains(string,symbol)
    assert res == expected



@pytest.mark.parametrize("string,symbol,expected",
[("Python","Py","thon"),
("Zero","ero","Z"),
("Verb","erb","V"),
("Wins","s","Win")
])
def test_delete_symbol_positive(string,symbol,expected):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(string,symbol)
    assert res == expected 


#Негативные сценария 

@pytest.mark.parametrize("input_word,expected",
[("",""),
("123abc","123abc"),
("123","123"),
("04 апреля","04 апреля"),
 ([""])
 ])
def test_capitalize_negative(input_word,expected):
    stringUtils = StringUtils()
    res = stringUtils.capitalize(input_word)
    assert res == expected


@pytest.mark.parametrize("input_word,expected",
[("",""),
("123abc","123abc"),
("123","123"),
("04 апреля","04 апреля"),
 ([""])
 ])
def test_trim_negative(input_word,expected):
    stringUtils = StringUtils()
    res = stringUtils.trim(input_word)
    assert res == expected


@pytest.mark.parametrize("string,symbol,expected",
[("",""),
("123abc","123abc"),
("123","123"),
("04 апреля","04 апреля"),
 ([""])
 ])
def test_contains_negative(string,symbol,expected):
    stringUtils = StringUtils()
    res = stringUtils.contains(string,symbol)
    assert res == expected

@pytest.mark.parametrize("string,symbol,expected",
[("",""),
("123abc","123abc"),
("123","123"),
("04 апреля","04 апреля"),
 ([""])
 ])

def test_delete_symbol_negative(string,symbol,expected):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(string,symbol)
    assert res == expected 

