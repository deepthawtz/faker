"""A library for generating fake user data"""
VERSION = (0,1,2)
__version__ = ".".join(map(str, VERSION))
__author__ = "Dylan Clendenin"
__contact__ = "dylan.clendenin@gmail.com"
__homepage__ = "https://github.com/deepthawtz/faker"
__all__ = ("Faker",)

import random
import warnings

from faker import data
from faker import patterns
from faker.utils import rand, numerify, domain, secondary_address

deprecation_message = """
This faker package is being deprecated September 15, 2016.

You should switch to using https://pypi.python.org/pypi/fake-factory instead.
After September 15, 2016 the PyPi faker package will be changing to that!
"""
warnings.simplefilter("always", PendingDeprecationWarning)
warnings.warn(deprecation_message, PendingDeprecationWarning)


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

    def __init__(self,
        seed=None, zip_type=None, min_age=None, max_age=None):

        self._names = None
        self._name_accesses = set()

        # set the type of zip to None (default), 5 or 9
        self.zip_type = zip_type if zip_type in [None, 5, 9] else None

        # set the minimum and maximum ages (swap if min > max)
        self.min_age = min_age if type(min_age) == int else 16
        self.max_age = max_age if type(max_age) == int else 80
        if self.min_age > self.max_age:
            self.min_age, self.max_age = self.max_age, self.min_age

        # set the random seed
        self.reset(seed)

    def _get_names(self):
        self._names = [rand(data.FIRST_NAMES), rand(data.LAST_NAMES)]
        self._name_accesses = set()

    def reset(self, seed=None):
        """Reset the seed for the random number generator.

        The seed can be any integer and using the same
        seed repeatedly will generate the same sequence
        of random numbers multiple times. If no seed (or
        an invalid seed) is given, the seed will be a
        new randomized value.
        """
        if seed is not None and type(seed) is int:
            random.seed(seed)
        else:
            random.seed()

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
        zips = { None:random.choice(["#####", "#####-####"]),
                 5:"#####",
                 9:"#####-####" }
        return numerify(zips[self.zip_type])

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
        return random.randint(self.min_age, self.max_age)

    def gender(self):
        return random.choice(["M","F"])

