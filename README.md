# Geograpic coordinate converter

Conversion tool for DMS, decimal degrees, and meters. You can install this into your QGIS Python distribution via the OSGeo4W shell using pip. 

```
pip install -i https://test.pypi.org/simple/ geogcoordconverter
```

There's currently three functions: `convert_dms_to_dd`, `convert_dd_to_dms`, `convert_meters_to_dd`. In order to use the functions, just import the `geogcoordconverter` package and the `converter` module.

```
import geogcoordconverter
from geogcoordconverter import converter
``` 