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
A port of Ruby's Faker library which is a port of Perl's Data::Faker library.

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

OR

    >>> from faker import Faker
    >>> f = Faker()
    >>> for i in range(3):
    ...     f.name()
    ...     f.username()
    ...     f.email()
    ...     f.phonenumber()
    ...     f.full_address()
    ...
    'Ola Rice'
    'orice'
    'orice@hotmail.com'
    '289-554-46105'
    '824 Colleen Square\nFrancescamouth, AK 65473'
    'Jaron Oberbrunner'
    'joberbrunner'
    'joberbrunner@gmail.com'
    '213-543-45170'
    '149 Fay Points 111\nWest Braulioland, MD 63587-2095'
    'Brielle Hegmann'
    'bhegmann'
    'bhegmann@hotmail.com'
    '553-104-17156'
    '96397 Colleen Square\nWest Braulioland, OH 75395'



Feedback
========
Any ideas where this should go? Features that would be useful? Bugs?
