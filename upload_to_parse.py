from parse_rest.connection import register
from parse_rest.connection import ParseBatcher
from parse_rest.datatypes import Object
import settings_local
import json

class Park(Object):
    pass

def chunks(l, n):
    if n<1:
        n=1
    return [l[i:i+n] for i in range(0, len(l), n)]

def upload_nice_json_to_parse():
    register(settings_local.APPLICATION_ID, settings_local.REST_API_KEY, master_key=settings_local.MASTER_KEY)

    park_objects = []

    with open('parks_nice.geojson') as nice_json_file:
        nice_json_data = json.load(nice_json_file)

        for park_json in nice_json_data:
            park_object = Park(geometry=park_json['geometry'], type=park_json['type'], properties=park_json['properties'])
            park_objects.append(park_object)

    chunked_arrays = chunks(park_objects, 50)
    batcher = ParseBatcher()

    for chunk in chunked_arrays:
        batcher.batch_save(chunk)

if __name__ == "__main__":
    objects = upload_nice_json_to_parse()

