#!/usr/bin/env python

# $Id$

import os
import ctypes

import geotrans2_lib

engine_errors = [key for key in dir(geotrans2_lib) if key.startswith('ENGINE')]

def setup_environment():
	data_path = os.path.join(os.path.dirname(__file__), 'data')
	os.environ.setdefault('GEOTRANS_DATA', data_path)

def handle_status(status):
	errors = [error for error in engine_errors if getattr(geotrans2_lib, error) & status]
	if errors:
		raise Exception(errors)

def initialize_engine():
	setup_environment()
	handle_status(geotrans2_lib.Initialize_Engine())

def get_datum_index(datum_code):
	index = ctypes.c_long(999)
	try:
		handle_status(geotrans2_lib.Get_Datum_Index(datum_code, ctypes.byref(index)))
	except Exception, e:
		print 'ignoring exception', e
	return index.value