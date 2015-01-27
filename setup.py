#!/usr/bin/env python

import os
import sys

import roboticeclient

from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'roboticeclient',
    'roboticeclient.control',
    'roboticeclient.robotice',
]

requires = """
requests==2.5.1
""".split()

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name='python-roboticeclient',
    version=roboticeclient.__version__,
    description='Python HTTP Robotice Client',
    long_description=readme + '\n\n' + history,
    author=roboticeclient.__author__,
    author_email='mail@majklk.cz',
    url='https://github.com/robotice/robotice',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE'], 'roboticeclient': ['*.pem']},
    package_dir={'roboticeclient': 'roboticeclient'},
    include_package_data=True,
    install_requires=requires,
    license=roboticeclient.__license__,
    zip_safe=False,
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