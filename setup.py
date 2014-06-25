#!/usr/bin/env python
"""
j2cli
==========

Command-line interface to [Jinja2](http://jinja.pocoo.org/docs/) for templating in shell scripts.

Features:

* Jinja2 templating
* Allows to use environment variables
* YAML or JSON data sources supported

Usage:

$ j2 config.j2 data.json --format=json
$ cat data.json | j2 config.j2

Based on [mattrobenolt/jinja2-cli](https://github.com/mattrobenolt/jinja2-cli)
"""

from setuptools import setup, find_packages

setup(
    name='j2cli',
    version='0.3.0-0',
    author='Mark Vartanyan',
    author_email='kolypto@gmail.com',

    url='https://github.com/kolypto/j2cli',
    license='BSD',
    description='Command-line interface to Jinja2 for templating in shell scripts.',
    long_description=__doc__,
    keywords=['Jinja2', 'templating', 'command-line', 'CLI'],

    packages=find_packages(),
    scripts=[],
    entry_points={
        'console_scripts': [
            'j2 = j2cli:main',
        ]
    },

    install_requires=[
        'jinja2 >= 2.7.2',
    ],
    include_package_data=True,
    zip_safe=False,

    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        #'Programming Language :: Python :: 3',
    ],
)
