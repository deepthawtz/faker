import random

import data
import patterns
from utils import _rand, _numerify, _bothify, _letterify

__all__ = ("Faker",)



class Faker(object):
    """
    The big fat Faker
    """

    def __init__(self):
        self._name = ""
        self._email = ""
        self._username = ""

    def name(self):
        """
        get a full fake name FIRST and LAST
        """
        self._name = " ".join([self.first_name(), self.last_name()])
        return self._name

    def first_name(self):
        """
        get just a first name
        """
        return _rand(data.FIRST_NAMES)

    def last_name(self):
        """
        get just a last name
        """
        return _rand(data.LAST_NAMES)

    def username(self):
        """
        get a fake username (e.g., like real websites require)
        """
        first, last = self._name.split()
        self._username = "".join([first[:1], last]).lower()
        return self._username

    def email(self):
        """
        get a fake email address
        """
        self._email = "@".join([self.username(), self._domain()])
        return self._email

    def _domain(self):
        """
        helper method for email(), returns a common email domain
        """
        return _rand(data.FREE_EMAIL)

    def full_address(self):
        """
        a full address: NUMBER, STREET, CITY, STATE and ZIP
        """
        return "%s\n%s, %s %s" % (self.street_address(), self.city(), self.state_abbr(), self.zip_code())

    def phonenumber(self):
        """
        get a phone number (e.g., ###-###-####)
        """
        return _numerify("###-###-#####")

    def street_address(self):
        """
        get a street address
        """
        return _numerify(random.choice(["##### %s" % patterns.STREET_NAME(),
                                         "#### %s Ave." % patterns.STREET_NAME(),
                                         "### %s St." % patterns.STREET_NAME(),
                                         "### %s %s" % (patterns.STREET_NAME(), self._secondary_address()),
                                         "#### %s %s" % (patterns.STREET_NAME(), self._secondary_address())]))

    def _secondary_address(self):
        """
        helper method for street_address(), returns an optional secondary street
        address, like Apt. number for example
        """
        return _numerify(random.choice(["Apt. ###", "Suite ###", ""]))

    def city(self):
        """
        get a fake city name
        """
        return patterns.CITY()

    def state_abbr(self):
        """
        get a state abbreviation like CA, OH, or FL. Etc...
        """
        return _rand(data.STATE_ABBR)

    def zip_code(self):
        """
        get a US zipcode
        """
        return _numerify(random.choice(["#####", "#####-####"]))

    def _uk_postcode(self):
        """
        coming soon? UK addresses
        """
        return _bothify(random.choice(["??# #??","??## #??"]))

    def lorem(self):
        """
        get a random paragraph of Latin words
        """
        paragraph = []
        word_list = data.WORDS.split()
        random.shuffle(word_list)
        for w in word_list:
            paragraph.append(w)
        return " ".join(paragraph)

