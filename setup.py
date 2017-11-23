#! /usr/bin/env python
from setuptools import setup, find_packages
from glob import glob

NAME = 'djsearch'
DESCRIPTION = 'Search tools for django appliation'
URL = 'https://github.com/hdknr/' + NAME
SCRIPTS = glob('scripts/*.py')
PACKAGES = [
    i for i in find_packages(exclude=['tests'])
    if '.' not in i]
VERSION = getattr(__import__(PACKAGES[0]),  '__version__')
REQUIRES = [
    i.strip() for i in
    open('requirements/pypi.txt').readlines() if i[0] != '#']
README = open('README.md').read()
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Library',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Simplifed BSD License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
]


setup(
    license='Simplfied BSD License',
    author='Hideki Nara of LaFoaglia,Inc.',
    author_email='gmail [at] hdknr.com',
    maintainer='LaFoglia,Inc.',
    maintainer_email='gmail [at] hdknr.com',
    classifiers=CLASSIFIERS,
    name=NAME,
    version=VERSION,
    url=URL,
    description=DESCRIPTION,
    download_url=URL,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=False,
    long_description=README,
    scripts=SCRIPTS,
    install_requires=REQUIRES,
)
