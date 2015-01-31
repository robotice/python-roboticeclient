#!/usr/bin/env python

import os
import sys

import roboticeclient

from codecs import open

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

requires = """
requests==2.5.1
""".split()

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='python-roboticeclient',
    version=roboticeclient.__version__,
    description='Python HTTP Robotice Client',
    long_description=readme,
    include_package_data=True,
    author=roboticeclient.__author__,
    author_email='mail@majklk.cz',
    url='https://github.com/robotice/python-roboticeclient',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={'': ['README', 'HISTORY'], 'roboticeclient': ['*.pem']},
    package_dir={'roboticeclient': 'roboticeclient'},
    install_requires=requires,
    license=roboticeclient.__license__,
    zip_safe=False,
    scripts=['bin/roboticeclient'],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)