import csv
import json

#Name csv
with open('places.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	geojson = {"type": "FeatureCollection"}
	logs = []
	for row in reader:
		logs.append(row)
	
	headers = logs[0][2:]
	dotList = []
	
	for dot in logs[1:]:
		properties = dot[2:]
		#Column 1 needs to be the latitude. Column 2 is longitude
		feeder = {"geometry": {
					"type": "Point",
					"coordinates": [ dot[0], dot[1] ]
				}, "type": "Feature",
				"properties": dict(zip(headers, properties))
			}
		dotList.append(feeder)
	
	geojson['features'] = dotList

	filename = 'points.js'
	file = open(filename, 'w')

	starter = 'var places = '

	file.write(starter)
	file.write(json.dumps(geojson, indent=4))

	
	
	
	