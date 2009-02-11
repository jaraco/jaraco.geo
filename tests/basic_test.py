from jaraco.geo.geotrans import *
from traceback import print_exc
try:
	initialize_engine()
	print get_datum_index('WGE')
except Exception, e:
	print_exc()
