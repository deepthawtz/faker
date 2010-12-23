"""A library for generating fake user data"""
VERSION = (0,0,2)
__version__ = ".".join(map(str, VERSION))
__author__ = "Dylan Clendenin"
__contact__ = "dylan.clendenin@gmail.com"
__homepage__ = "https://github.com/deepthawtz/faker"
__all__ = ("Faker",)

import random

import data
import patterns
from utils import *



class Faker(object):

    def __init__(self):
        self._name = ""
        self._email = ""
        self._username = ""

    def name(self):
        self._name = " ".join([self.first_name(), self.last_name()])
        return self._name

    def first_name(self):
        return rand(data.FIRST_NAMES)

    def last_name(self):
        return rand(data.LAST_NAMES)

    def username(self):
        first, last = self._name.split()
        self._username = "".join([first[:1], last]).lower().replace("'", "")
        return self._username

    def email(self):
        self._email = "@".join([self.username(), domain()])
        return self._email

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

