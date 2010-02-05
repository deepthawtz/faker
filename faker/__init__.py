"""
Faker
"""
import random
from faker.data import *
from faker.patterns import *
from faker.utils import __rand, __numerify, __letterify, __bothify


__all__ = ["Faker"]


class Faker(object):
    def __init__(self):
        self._name = ""
        self._email = ""
        self._username = ""

    def name(self):
        self._name = " ".join([self._first_name(), self._last_name()])
        return self._name

    def _first_name(self):
        return __rand(FIRST_NAMES)

    def _last_name(self):
        return __rand(LAST_NAMES)

    def username(self):
        first, last = self._name.split()
        self._username = "".join([first[:1], last]).lower()
        return self._username

    def email(self):
        self._email = "@".join([self.username(), self._domain()])
        return self._email

    def _domain(self):
        return __rand(FREE_EMAIL)

    def full_address(self):
        return "%s\n%s, %s %s" % (self._street_address, self._city, self._state_abbr, self._zip_code)

    def phonenumber(self):
        return __numerify("###-###-#####")

    def _street_address(self):
        return __numerify(random.choice(["##### %s" % __rand(STREET_NAME),
                                         "#### %s" % __rand(STREET_NAME),
                                         "### %s" % __rand(STREET_NAME),
                                         "### %s %s" % (__rand(STREET_NAME), _secondary_address),
                                         "#### %s %s" % (__rand(STREET_NAME), _secondary_address)]))

    def _secondary_address(self):
        return __rand(__numerify(["Apt. ###", "Suite ###"]))

    def _city(self):
        return __rand(CITY)

    def _state_abbr(self):
        return __rand(STATE_ABBR)

    def _zip_code(self):
        return __numerify(random.choice(["#####", "#####-####"]))

    def _uk_postcode(self):
        return __bothify(__rand(["??# #??","??## #??"]))

    def lorem(self):
        paragraph = []
        word_list = WORDS.split()
        random.shuffle(word_list)
        for w in word_list:
            paragraph.append(w)
        return " ".join(paragraph)
