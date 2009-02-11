#!/usr/bin/env python

# $Id$

import os
import ctypes
from jaraco.windows import environ

class run_in_dir(object):
	def __init__(self, dir):
		self.orig = os.getcwd()
		os.chdir(dir)
	
	def __del__(self):
		os.chdir(self.orig)

def run_in_data():
	# short circuit
	return
	data_path = getenv('GEOTRANS_DATA')
	return run_in_dir(data_path)

getenv = ctypes.cdll.msvcrt.getenv
getenv.restype = ctypes.c_char_p
wgetenv = ctypes.cdll.msvcrt._wgetenv
wgetenv.restype = ctypes.c_wchar_p
wgetenv.argtypes = [ctypes.c_wchar_p]
putenv = ctypes.cdll.msvcrt._putenv
wputenv = ctypes.cdll.msvcrt._wputenv
wputenv.argtypes = [ctypes.c_wchar_p]

def do_putenv(*pair):
	#putenv("=".join(pair))
	wputenv("=".join(pair))
	
def setup_environment():
	data_path = os.path.join(os.path.dirname(__file__), 'data')
	assert os.path.exists(os.path.join(data_path, '7_param.dat'))
	key = 'GEOTRANS_DATA'
	do_putenv(key, data_path)
	assert getenv(key) == data_path
	assert wgetenv(key) == data_path

setup_environment()

import geotrans2_lib

engine_errors = [key for key in dir(geotrans2_lib) if key.startswith('ENGINE')]


def handle_status(status):
	errors = [error for error in engine_errors if getattr(geotrans2_lib, error) & status]
	if errors:
		raise Exception(errors)

def initialize_engine():
	setup_environment()
	handle = run_in_data()
	handle_status(geotrans2_lib.Initialize_Engine())

def get_datum_index(datum_code):
	handle = run_in_data()
	index = ctypes.c_long(999)
	try:
		handle_status(geotrans2_lib.Get_Datum_Index(datum_code, ctypes.byref(index)))
	except Exception, e:
		print 'ignoring exception', e
	return index.value