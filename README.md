CSV to GeoJSON
=========

This is a script written to turn a spreadsheet of latitude and longitude points into a geojson file for use with the [leaflet.js] [1] javascript mapping library.

The structure of your .csv file is key. You __must have__ the following two cells in your data:
  - Latitude (it __must be__ the first column)
  - Longitude (it __must be__ the second column)

The script reads your file, takes your latitude and longitude points, and sets them to the coordinates list that leaflet.js uses to plot your location. 

The __places.csv__ file provided is a good template to follow. You can add as many columns to the right of the **LON** column. The script will always return an object with the name of the column as the key. This builds out your properties object, which you can use in your leaflet.js program.


This pairs well with the Texas A&M geocode script I wrote, which you can [find here][2].

The files:
  - geojson.py: the script
  - places.csv: A dummy sheet of lat/longs to turn into geojson
  - places.js: the resulting geojson after teh script runs.


License
----

MIT


[1]:http://leafletjs.com
[2]:https://github.com/Jonnyd55/geocode_A-M
