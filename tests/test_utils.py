import re

from faker.utils import *


def test_rand():
    possible = ["one", "two", "three"]
    string = "one two three"
    output = rand(string)
    assert output in possible

def test_numerify():
    pattern = re.compile(r"\d{3}-\d{4}")
    output = numerify("###-####")
    assert pattern.match(output)

def test_letterify():
    pattern = re.compile(r"[A-Z]{4}")
    output = letterify("????")
    assert pattern.match(output)

def test_bothify():
    pattern = re.compile(r"[A-Z]{2}\d{1}[A-Z]\d{3}")
    output = bothify("??#?###")
    assert pattern.match(output)

