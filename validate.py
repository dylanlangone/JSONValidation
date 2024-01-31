import json
import argparse
from jsonschema import validate

# Describe what kind of json you expect.
schema1 = {
    "type": "object",
    "properties": {
        "unit_name": {"type" : "string"},
        "devices" : {
            "type" : "array",
            "minItems" : 1,
            "items" : {
                "type" : "object",
                "properties" : {
                    "capacity" : {"type" : "string"},
                    "storage_type" : {"type" : "string"}
                },
                "required" : ["capacity", "storage_type"]
            }
        }
    },
    "required": ["unit_name", "devices"]
    
}

""" # this JSON instance is not a valid object because there is no key for "2017-c.2"
instance = {
    "2003-xyz.2": [
        {
            "capacity" : "239849820954321",
            "storage_type" : "block"
        }
    ]
} """

# this is a valid JSON object because there is now a key for both 2017-c.2 
# and for the devices contained within that unit
correct_instance = {
    "unit_name" : "2003-xyz.2",
    "devices" : [
        {
            "capacity" : "239849820954321",
            "storage_type" : "block"
        },

        {
            "capacity" : "459835489",
            "storage_type" : "block"
        }
    ]
}

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="read in a JSON file with the specified filename")
args = parser.parse_args()

with open(args.filename) as f:
    instance = f.read()

correct_instance = json.loads(instance)

# if the schema is valid and the instance matches the schema 
# there will be no exceptions raised
validate(instance=correct_instance, schema=schema1)

print("JSON object present in ", args.filename, " is valid according to specified JSON schema")
