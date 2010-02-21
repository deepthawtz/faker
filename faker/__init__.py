"""
Faker
"""

import random
import data
import patterns
from utils import _rand, _numerify, _bothify, _letterify


__all__ = ("Faker",)


class Faker(object):

    def __init__(self):
        self._name = ""
        self._email = ""
        self._username = ""

    def name(self):
        self._name = " ".join([self._first_name(), self._last_name()])
        return self._name

    def _first_name(self):
        return _rand(data.FIRST_NAMES)

    def _last_name(self):
        return _rand(data.LAST_NAMES)

    def username(self):
        first, last = self._name.split()
        self._username = "".join([first[:1], last]).lower()
        return self._username

    def email(self):
        self._email = "@".join([self.username(), self._domain()])
        return self._email

    def _domain(self):
        return _rand(data.FREE_EMAIL)

    def full_address(self):
        return "%s\n%s, %s %s" % (self._street_address(), self._city(), self._state_abbr(), self._zip_code())

    def phonenumber(self):
        return _numerify("###-###-#####")

    def _street_address(self):
        return _numerify(random.choice(["##### %s" % patterns.STREET_NAME(),
                                         "#### %s Ave." % patterns.STREET_NAME(),
                                         "### %s St." % patterns.STREET_NAME(),
                                         "### %s %s" % (patterns.STREET_NAME(), self._secondary_address()),
                                         "#### %s %s" % (patterns.STREET_NAME(), self._secondary_address())]))

    def _secondary_address(self):
        return _numerify(random.choice(["Apt. ###", "Suite ###", ""]))

    def _city(self):
        return patterns.CITY()

    def _state_abbr(self):
        return _rand(data.STATE_ABBR)

    def _zip_code(self):
        return _numerify(random.choice(["#####", "#####-####"]))

    def _uk_postcode(self):
        return _bothify(random.choice(["??# #??","??## #??"]))

    def lorem(self):
        paragraph = []
        word_list = data.WORDS.split()
        random.shuffle(word_list)
        for w in word_list:
            paragraph.append(w)
        return " ".join(paragraph)

