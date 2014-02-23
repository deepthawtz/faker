import random

from faker import data
from faker.utils import rand



CITY = lambda: random.choice([
    " ".join([rand(data.CITY_PREFIX), "".join([rand(data.FIRST_NAMES), rand(data.CITY_SUFFIX)])]),
    " ".join([rand(data.CITY_PREFIX), rand(data.FIRST_NAMES)]),
    "".join([rand(data.FIRST_NAMES), rand(data.CITY_SUFFIX)]),
    "".join([rand(data.LAST_NAMES), rand(data.CITY_SUFFIX)]),
])

STREET_NAME = lambda: random.choice([
    " ".join([rand(data.LAST_NAMES), rand(data.STREET_SUFFIX)]),
    " ".join([rand(data.FIRST_NAMES), rand(data.STREET_SUFFIX)])
])

COMPANY_NAME = lambda: random.choice([
    "".join([rand(data.COMPANY_NAME_PREFIX), rand(data.COMPANY_NAME_SUFFIX)]),
    "".join([rand(data.COMPANY_NAME_PREFIX).capitalize(), rand(data.COMPANY_NAME_SUFFIX)]),
    "".join([rand(data.COMPANY_NAME_PREFIX).capitalize(), rand(data.COMPANY_NAME_SUFFIX).capitalize()]),
    "%s %s" % ("".join([rand(data.COMPANY_NAME_PREFIX).capitalize(), rand(data.COMPANY_NAME_SUFFIX)]), rand(data.COMPANY_NAME_EXTRA).capitalize())
])

