# -*- coding: UTF-8 -*-

""" Setup script for building jaraco-util distribution

Copyright © 2004-2009 Jason R. Coombs
"""

from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages
from jaraco.util.package import read_long_description

__author__ = 'Jason R. Coombs <jaraco@jaraco.com>'
__version__ = '$Rev$'[6:-2]
__svnauthor__ = '$Author$'[9:-2]
__date__ = '$Date$'[7:-2]

name = 'jaraco.geo'

setup (
	name = name,
	version = '1.0',
	description = 'Geographic coordinates package',
	long_description = read_long_description(__file__),
	author = 'Jason R. Coombs',
	author_email = 'jaraco@jaraco.com',
	url = 'http://pypi.python.org/pypi/'+name,
	packages = find_packages(exclude=['ez_setup', 'tests', 'examples']),
	namespace_packages = ['jaraco',],
	license = 'MIT',
	classifiers = [
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Programming Language :: Python",
	],
	entry_points = {
		'console_scripts': [
			],
	},
	install_requires=[
		'jaraco.util',
	],
	extras_require = {
	},
	dependency_links = [
	],
	tests_require=[
		'nose>=0.10',
	],
	test_suite = "nose.collector",
)
