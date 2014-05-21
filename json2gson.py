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
    map_data = {
        "id": "bnookala.ia5763g5",
        "type": "FeatureCollection",
        "features": [],
    }

    for index, row in enumerate(data):
        marker = {
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
            continue

        marker["properties"]["title"] = name
        marker["geometry"]["coordinates"] = [float(longitude), float(latitude)]

        map_data["features"].append(marker)

    return map_data

if __name__ == '__main__':
    json2gson()
