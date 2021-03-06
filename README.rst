.. image:: https://img.shields.io/pypi/v/jaraco.geo.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/jaraco.geo.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/jaraco.geo

.. image:: https://github.com/jaraco/jaraco.geo/workflows/tests/badge.svg
   :target: https://github.com/jaraco/jaraco.geo/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. .. image:: https://readthedocs.org/projects/skeleton/badge/?version=latest
..    :target: https://skeleton.readthedocs.io/en/latest/?badge=latest

Geographic support library

Requirements
============

The current geotrans2 dynamic libraries are currently built only
for Windows, so support for other platforms is currently not present.
However, the DMS class should be usable in a pure Python environment.

Contents
========

``jaraco.geo`` includes an object named DMS for storing and manipulating
values in degrees, minutes, and seconds. See the jaraco.geo module for
details and documentation.

``jaraco.geo`` also implements geotrans2 by the `NGA
<http://www.nga.mil>`_. See the tests directory in the
repository for sample usage.
