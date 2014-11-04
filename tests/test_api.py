import re
from faker import Faker

from nose.tools import *


def setup():
    global f
    f = Faker()

def test_instance():
    ok_(isinstance(f, Faker), msg="object should be instance of Faker")

def test_name():
    pattern = re.compile(r"(\w+\.? ?){2,3}")
    name = f.name()
    ok_(pattern.match(name))

def test_username():
    pattern = re.compile(r"[a-z]+")
    username = f.username()
    ok_(pattern.match(username))

def test_email():
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

def test_company():
    pattern = re.compile(r"\w{1,3}")
    for i in range(10):
        company = f.company()
        ok_(pattern.match(company))

def test_username_first():
    f = Faker()
    f.username()

def test_username_multiple():
    f = Faker()
    v1 = f.username()
    v2 = f.username()
    ok_(v1 != v2)

def test_name_multiple():
    f = Faker()
    v1 = f.name()
    v2 = f.name()
    ok_(v1 != v2)

def test_name_correspondance1():
    f = Faker()
    f1 = f.first_name()
    n1 = f.name()
    f2 = f.first_name()
    n2 = f.name()

    # Check they correspond as we expect
    ok_(f1 in n1)
    ok_(f2 in n2)

def test_name_correspondance2():
    f = Faker()
    # Opposite order to above
    n1 = f.name()
    f1 = f.first_name()
    n2 = f.name()
    f2 = f.first_name()

    # Check they correspond as we expect
    ok_(f1 in n1)
    ok_(f2 in n2)


def test_age():
    f = Faker()
    age1 = f.age()
    age2 = f.age()
    ok_(isinstance(age1, int))
    ok_(isinstance(age2, int))

def test_seed():
    import sys
    if sys.version_info.major == 2:
        initname = "Vita Kertzmann"
    elif sys.version_info.major == 3:
        initname = "Layla Cassin"
    f = Faker(1234)
    name1 = f.name()
    name2 = f.name()
    ok_(name1 == initname)
    ok_(name1 != name2)
    f.reset(1234)
    name2 = f.name()
    ok_(name1 == name2)
    

    
