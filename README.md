[![Build Status](https://travis-ci.org/deepthawtz/faker.png?branch=master)](https://travis-ci.org/deepthawtz/faker)

NOTE: This package is being deprecated
======================================

You should use [fake-factory](https://pypi.python.org/pypi/fake-factory)
instead. After Sept 15, 2016 the PyPi `faker` package will point to new
[faker](https://github.com/joke2k/faker).



        .....                            ..
     .H8888888x.  '`+              < .z@8"`
    :888888888888x.  !              !@88E                      .u    .
    8~    `"*88888888"       u      '888E   u         .u     .d88B :@8c
    !      .  `f""""      us888u.    888E u@8NL    ud8888.  ="8888f8888r
     ~:...-` :8L <)88: .@88 "8888"   888E`"88*"  :888'8888.   4888>'88"
        .   :888:>X88! 9888  9888    888E .dN.   d888 '88%"   4888> '
     :~"88x 48888X ^`  9888  9888    888E~8888   8888.+"      4888>
    <  :888k'88888X    9888  9888    888E '888&  8888L       .d888L .+
      d8888f '88888X   9888  9888    888E  9888. '8888c. .+  ^"8888*"
     :8888!    ?8888>  "888*""888" '"888*" 4888"  "88888%       "Y"
     X888!      8888~   ^Y"   ^Y'     ""    ""      "YP'
     '888       X88f
      '%8:     .8*"
         ^----~"`

Faker
=====

A Python library for generating fake user data.
Perl's got one, Ruby's got one, now Pythonistas envy no longer.

Usage
=====

    >>> from faker import Faker
    >>> f = Faker()
    >>> f.name()
    "Milli Vanilli"
    >>> f.username()
    "mvanilli"
    >>> f.email()
    "mvanilli@hotmail.com"
    >>> f.company()
    "Scrodiant Labs"

OR

    >>> from faker import Faker
    >>> f = Faker()
    >>> for i in range(3):
    ...     f.name()
    ...     f.username()
    ...     f.email()
    ...     f.phonenumber()
    ...     f.full_address()
    ...     f.company()
    ...
    "Ola Rice"
    "orice"
    "orice@hotmail.com"
    "289-554-46105"
    "824 Colleen Square\nFrancescamouth, AK 65473"
    "Yeddjam"
    "Jaron Oberbrunner"
    "joberbrunner"
    "joberbrunner@gmail.com"
    "213-543-45170"
    "149 Fay Points 111\nWest Braulioland, MD 63587-2095"
    "Plurbee"
    "Brielle Hegmann"
    "bhegmann"
    "bhegmann@hotmail.com"
    "553-104-17156"
    "96397 Colleen Square\nWest Braulioland, OH 75395"
    "Twispace"


Installation
============

pip:

    pip install faker

source:

    git clone git@github.com:deepthawtz/faker.git
    cd faker
    python setup.py install

