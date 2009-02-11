# This test is a translation of the example given in engine/docs/abstract.doc

"""
Here's the C pseudo-code

#define PI         3.14159265358979323e0  
Parameters:
  long status;
  long datum_index;
  double ce90, le90, se90;
  Geodetic_Parameters input_params;
  Geodetic_Tuple input_coords;
  Mercator_Parameters output_params;
  Mercator_Tuple output_coords; 
Inputs:
  ce90 = 1.0;
  le90 = 1.0;
  se90 = 1.0;
  input_params.height_type = Ellipsoid_Height;
  input_coords.latitude = -35.0 * PI/180.0;
  input_coords.longitude = 75.0 * PI/180.0;
  input_coords.height = 0.0;
  output_params.central_meridian = 0.0;
  output_params.latitude_of_true_scale = 0.0;
  output_params.scale_factor = 1.0;
  output_params.false_easting = 0.0;
  output_params.false_northing = 0.0; 
Function Call:
  status = Initialize_Engine();
  status = Get_Datum_Index ("WGE", &datum_index);
  status = Set_Datum (Interactive, Input, datum_index);
  status = Set_Coordinate_System (Interactive, Input, Geodetic);
  status = Set_Geodetic_Params (Interactive, Input, input_params);
  status = Set_Geodetic_Coordinates (Interactive, Input, input_coords);
  status = Set_Conversion_Errors(Interactive, ce90, le90, se90);
  status = Set_Datum (Interactive, Output, datum_index);
  status = Set_Coordinate_System (Interactive, Output, Mercator);
  status = Set_Mercator_Params (Interactive, Output, output_params);
  status = Convert(Interactive);
  status = Get_Mercator_Coordinates (Interactive, Output, &output_coords);
  status = Get_Conversion_Errors (Interactive, &ce90, &le90, &se90); 
Outputs:
output_coords.easting:	8348961.81
output_coords.northing:	-4139372.76
output_coords.height:		0.0
ce90:		1.0
le90		1.0
se90		1.0
"""

from ctypes import *
from jaraco.geo.geotrans import *
from jaraco.geo.geotrans2_lib import *

import math
PI = math.pi

datum_index = c_long()

ce90 = c_double(1.0)
le90 = c_double(1.0)
se90 = c_double(1.0)

input_params = Geodetic_Parameters()
input_params.height_type = Ellipsoid_Height
input_coords = Geodetic_Tuple()
input_coords.latitude = -35.0*PI/180.0
input_coords.longitude = 75.0*PI/180.0
input_coords.height = 0.0
output_params = Mercator_Parameters()
output_params.central_meridian = 0.0
output_params.latitude_of_true_scale = 0.0
output_params.scale_factor = 1.0
output_params.false_easting = 0.0
output_params.false_northing = 0.0 
output_coords = Mercator_Tuple()

status = Initialize_Engine();
status = Get_Datum_Index ("WGE", datum_index);
status = Set_Datum (Interactive, Input, datum_index);
status = Set_Coordinate_System (Interactive, Input, Geodetic);
status = Set_Geodetic_Params (Interactive, Input, input_params);
status = Set_Geodetic_Coordinates (Interactive, Input, input_coords);
status = Set_Conversion_Errors(Interactive, ce90, le90, se90);
status = Set_Datum (Interactive, Output, datum_index);
status = Set_Coordinate_System (Interactive, Output, Mercator);
status = Set_Mercator_Params (Interactive, Output, output_params);
status = Convert(Interactive);
status = Get_Mercator_Coordinates (Interactive, Output, output_coords);
status = Get_Conversion_Errors (Interactive, ce90, le90, se90); 

print 'output_coords.easting:  %10.2f' % output_coords.easting
print 'output_coords.northing: %10.2f' % output_coords.northing
print 'ce90: %.1f' % ce90.value
print 'le90: %.1f' % le90.value
print 'se90: %.1f' % se90.value