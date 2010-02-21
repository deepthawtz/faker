import random

import data
from utils import _rand


CITY = lambda: random.choice([
    " ".join([_rand(data.CITY_PREFIX), "".join([_rand(data.FIRST_NAMES), _rand(data.CITY_SUFFIX)])]),
    " ".join([_rand(data.CITY_PREFIX), _rand(data.FIRST_NAMES)]),
    "".join([_rand(data.FIRST_NAMES), _rand(data.CITY_SUFFIX)]),
    "".join([_rand(data.LAST_NAMES), _rand(data.CITY_SUFFIX)]),
])

STREET_NAME = lambda: random.choice([
    " ".join([_rand(data.LAST_NAMES), _rand(data.STREET_SUFFIX)]),
    " ".join([_rand(data.FIRST_NAMES), _rand(data.STREET_SUFFIX)])
])
