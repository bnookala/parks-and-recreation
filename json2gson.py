import json

JSON_FILE = 'parks.json'
GSON_FILE = 'parks.geojson'

def json2gson():
    with open(JSON_FILE) as json_file:
        json_data = json.load(json_file)
        park_data = format_json_to_gson(json_data['data'])

    with open(GSON_FILE, 'w') as gson_file:
        json.dump(park_data, gson_file)

def format_json_to_gson(data):
    map_data = []
    outliers = []

    for index, row in enumerate(data):
        marker = {
            "type": "Feature",
            "geometry": {
                "coordinates": [],
                "type": "Point"
            },
            "properties": {
                "description": "",
                "marker-color": "#1087bf",
                "marker-size": "medium",
                "marker-symbol": "garden",
                "title": ""
            }
        }

        # First index contains nothing useful.
        if index == 0:
            continue

        name = row[8]
        address = row[18]

        latitude = address[1]
        longitude = address[2]

        if not latitude or not longitude:
            outliers.append(row)
            continue

        marker["properties"]["title"] = name
        marker["properties"]["description"] = row[9]
        marker["geometry"]["coordinates"] = [float(longitude), float(latitude)]

        map_data.append(marker)

    for outlier in outliers:
        name = outlier[8]

        marker = {
            "type": "Feature",
            "geometry": {
                "coordinates": [],
                "type": "Point"
            },
            "properties": {
                "description": "",
                "marker-color": "#1087bf",
                "marker-size": "medium",
                "marker-symbol": "garden",
                "title": ""
            }
        }

        latitude, longitude = json.loads(outlier[7])['invalidCells']['1685357'].split('(')[1][:-1].split(',')

        if not latitude or not longitude:
            continue

        marker["properties"]["title"] = name
        marker["properties"]["description"] = outlier[9]
        marker["geometry"]["coordinates"] = [float(longitude), float(latitude)]

        map_data.append(marker)

    return map_data

if __name__ == '__main__':
    json2gson()
