import re
from faker import Faker

from nose.tools import *


def setup():
    global f
    f = Faker()

def test_instance():
    ok_(isinstance(f, Faker), msg="object should be instance of Faker")

def test_fake_name():
    pattern = re.compile(r"(\w+\.? ?){2,3}")
    name = f.name()
    ok_(pattern.match(name))

def test_username():
    pattern = re.compile(r"[a-z]+")
    username = f.username()
    ok_(pattern.match(username))

def test_fake_email():
    pattern = re.compile(r".+@.+\.\w+")
    email = f.email()
    ok_(pattern.match(email))

def test_lorem():
    pattern = re.compile(r"\w*")
    paragraph = f.lorem()
    ok_(pattern.match(paragraph))

def test_address():
    pattern = re.compile(r"""(\d+)\s+           # first numbers
                             (.*)(\d+)?\n       # street address
                             (.*),\s+           # city
                             ([A-Z][A-Z])\s+    # state
                             (\d{5})(-\d{4})?   # zip
                          """, re.X)

    # test a variety of combos
    for i in range(10):
        address = f.full_address()
        ok_(pattern.match(address))

def test_phonenumber():
    pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
    phonenumber = f.phonenumber()
    ok_(pattern.match(phonenumber))
