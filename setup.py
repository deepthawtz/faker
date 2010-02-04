#!/usr/bin/env python

from distutils.core import setup

setup(name="Faker",
      version="0.0.1",
      description="A port of Ruby's Faker library for generating fake user data",
      long_description="Often you want to generate user data but without all the thinking and typing. This is a library for that.",
      author="Dylan Clendenin",
      author_email="dylan.clendenin@gmail.com",
      url="http://github.com/deepthawtz/faker",
      py_modules=["faker"],
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