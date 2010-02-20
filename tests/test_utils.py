import re

from faker.utils import _rand, _numerify, _letterify, _bothify


def test_rand():
    possible = ["one", "two", "three"]
    string = "one two three"
    output = _rand(string)
    assert output in possible

def test_numerify():
    pattern = re.compile(r"\d{3}-\d{4}")
    output = _numerify("###-####")
    assert pattern.match(output)

def test_letterify():
    pattern = re.compile(r"[A-Z]{4}")
    output = _letterify("????")
    assert pattern.match(output)

def test_bothify():
    pattern = re.compile(r"[A-Z]{2}\d{1}[A-Z]\d{3}")
    output = _bothify("??#?###")
    assert pattern.match(output)