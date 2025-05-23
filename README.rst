.. image:: https://img.shields.io/pypi/v/jaraco.geo.svg
   :target: https://pypi.org/project/jaraco.geo

.. image:: https://img.shields.io/pypi/pyversions/jaraco.geo.svg

.. image:: https://github.com/jaraco/jaraco.geo/actions/workflows/main.yml/badge.svg
   :target: https://github.com/jaraco/jaraco.geo/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. .. image:: https://readthedocs.org/projects/PROJECT_RTD/badge/?version=latest
..    :target: https://PROJECT_RTD.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2025-informational
   :target: https://blog.jaraco.com/skeleton

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
