import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "exscientia_code_challenge",
    version = "0.0.1",
    author = "Arvinder Palaha",
    author_email = "arvinder.palaha@googlemail.com",
    description = ("My play with the Exscientia coding challenge"),
    license = "MIT",
    url = "https://github.com/arvinder-palaha/exscientia_coding_challenge",
    packages=['an_example_pypi_project', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
)