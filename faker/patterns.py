from faker.data import *
from faker.utils import __rand

CITY = [
    "%s %s%s" % (CITY_PREFIX, __rand(FIRST_NAMES), CITY_SUFFIX),
    "%s %s" % (CITY_PREFIX, __rand(FIRST_NAMES)),
    "%s%s" % (__rand(FIRST_NAMES), CITY_SUFFIX),
    "%s%s" % (__rand(LAST_NAMES), CITY_SUFFIX),
]

STREET_NAME = [
    " ".join([__rand(LAST_NAMES), __rand(STREET_SUFFIX)]),
    " ".join([__rand(FIRST_NAMES), __rand(STREET_SUFFIX)])
]
