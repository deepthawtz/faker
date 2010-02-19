import data
from utils import _rand

CITY = [
    "%s %s%s" % (_rand(data.CITY_PREFIX), _rand(data.FIRST_NAMES), _rand(data.CITY_SUFFIX)),
    "%s %s" % (_rand(data.CITY_PREFIX), _rand(data.FIRST_NAMES)),
    "%s%s" % (_rand(data.FIRST_NAMES), _rand(data.CITY_SUFFIX)),
    "%s%s" % (_rand(data.LAST_NAMES), _rand(data.CITY_SUFFIX)),
]

STREET_NAME = [
    " ".join([_rand(data.LAST_NAMES), _rand(data.STREET_SUFFIX)]),
    " ".join([_rand(data.FIRST_NAMES), _rand(data.STREET_SUFFIX)])
]
