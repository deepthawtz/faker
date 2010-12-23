#!/usr/bin/env python

import codecs
from setuptools import setup, find_packages
import faker

setup(name="Faker",
      version=faker.__version__,
      description=faker.__doc__,
      long_description=codecs.open("README.txt", "r", "utf-8").read(),
      author=faker.__author__,
      author_email=faker.__contact__,
      url=faker.__homepage__,
      packages=find_packages(),
      test_suite="nose.collector",
      tests_require=["nose"],
      platforms="any",
      keywords="testing data generation",
      classifiers=[
          "Development Status :: 2 - Pre-Alpha",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Testing",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          ],
      license="MIT",
)
