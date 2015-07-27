#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()


setup(
    name='coveralls_trial',
    version='0.1.0',
    description="Coveralls unicode/utf-8 trial",
    long_description=readme,
    author="Alex Willmer",
    author_email='alex@moreati.org.uk',
    url='https://github.com/moreati/coveralls-trial',
    packages=[
        'coveralls_trial',
    ],
    include_package_data=True,
    license="BSD",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
)
