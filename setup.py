#!/usr/bin/env python

from setuptools import setup, find_packages

setup (
    name = "inexactsearch",
    version = "0.1",
    url = "http://silpa.org.in/ApproxSearch",
    license = "LGPL-3.0",
    author = "Santhosh Thottingal",
    author_email = "santhosh.thottingal@gmail.com",
    description = "Fuzzy String Search for Indian languages",
    long_description= "This library provides fuzzy string search\
for Indian languages using Indic Soundex module.",
    packages = find_packages('inexactsearch'),
    include_package_data = True,
    setup_requires = ['setuptools-git'],
    install_requires = ['setuptools','soundex'],
    zip_safe = False,
    )
