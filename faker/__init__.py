"""A library for generating fake user data"""
VERSION = (0,0,4)
__version__ = ".".join(map(str, VERSION))
__author__ = "Dylan Clendenin"
__contact__ = "dylan.clendenin@gmail.com"
__homepage__ = "https://github.com/deepthawtz/faker"
__all__ = ("Faker",)

import random

from faker import data
from faker import patterns
from faker.utils import rand, numerify, domain, secondary_address


# Decorator for methods that need _get_names.  This ensures that if we
# repeatedly use one method, we get fresh names, but if we cycle through the
# methods, we get a set of names/email addresses that correspond. The individual
# methods must not call each other for this to work.
def uses_names(func):
    def _wrapped(self):
        if not self._name_accesses or func.__name__ in self._name_accesses:
            self._get_names()
        self._name_accesses.add(func.__name__)
        return func(self)
    _wrapped.__name__ = func.__name__
    return _wrapped

class Faker(object):

    def __init__(self):
        self._names = None
        self._name_accesses = set()

    def _get_names(self):
        self._names = [rand(data.FIRST_NAMES), rand(data.LAST_NAMES)]
        self._name_accesses = set()

    @uses_names
    def name(self):
        return " ".join(self._names)

    @uses_names
    def first_name(self):
        return self._names[0]

    @uses_names
    def last_name(self):
        return self._names[1]

    @uses_names
    def username(self):
        first, last = self._names
        return "".join([first[:1], last]).lower().replace("'", "")

    @uses_names
    def email(self):
        first, last = self._names
        return ("%s%s@%s" % (first[:1], last, domain())).lower().replace("'", "")

    def full_address(self):
        return "%s\n%s, %s %s" % (self.street_address(), self.city(), self.state(), self.zip_code())

    def phonenumber(self):
        return numerify("###-###-#####")

    def street_address(self):
        return numerify(random.choice(["##### %s" % patterns.STREET_NAME(),
                                         "#### %s Ave." % patterns.STREET_NAME(),
                                         "### %s St." % patterns.STREET_NAME(),
                                         "### %s %s" % (patterns.STREET_NAME(), secondary_address()),
                                         "#### %s %s" % (patterns.STREET_NAME(), secondary_address())]))

    def city(self):
        return patterns.CITY()

    def state(self):
        return rand(data.STATE_ABBR)

    def zip_code(self):
        return numerify(random.choice(["#####", "#####-####"]))

    def company(self):
        return patterns.COMPANY_NAME()

    def lorem(self):
        paragraph = []
        word_list = data.WORDS.split()
        random.shuffle(word_list)
        for w in word_list:
            paragraph.append(w)
        return " ".join(paragraph)

    def age(self):
        return random.randint(16, 80)

