import re

from faker import Faker

f = Faker()

def test_instance():
    assert isinstance(f, Faker)

def test_fake_name():
    pattern = re.compile(r"(\w+\.? ?){2,3}")
    name = f.name()
    assert pattern.match(name)

def test_username():
    pattern = re.compile(r"[a-z]+")
    username = f.username()
    assert pattern.match(username)

def test_fake_email():
    pattern = re.compile(r".+@.+\.\w+")
    email = f.email()
    assert pattern.match(email)

def test_lorem():
    pattern = re.compile(r"\w*")
    paragraph = f.lorem()
    assert pattern.match(paragraph)

def test_address():
    pattern = re.compile(r"""(\d+)\s+           # first numbers
                             (.*)(\d+)?\n       # street address
                             (.*),\s+           # city
                             ([A-Z][A-Z])\s+    # state
                             (\d{5})(-\d{4})?   # zip
                          """, re.X)
    # to test a variety of combos
    for i in range(10):
        address = f.full_address()
        assert pattern.match(address)

def test_phonenumber():
    pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
    phonenumber = f.phonenumber()
    assert pattern.match(phonenumber)
