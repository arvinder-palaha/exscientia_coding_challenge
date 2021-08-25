import json
from jsonschema import validate

def get_schema():
    """Load a schema"""
    with open('schema.json', 'r') as file:
        schema = json.load(file)
    return schema

def validate_json(json_data):
    """Test json data against the schema"""
    execute_api_schema = get_schema()

    try:
        validate(instance=json_data, schema=execute_api_schema)
    except Exception as err:
        print(err)
        return False, err
    
    return True, "JSON data is valid"

def detect_encoding(filename):
    with open(filename, 'rb') as file:
        encoding = chardet.detect(file.read())['encoding']
        return encoding


print(detect_encoding('schema.json'))
print(detect_encoding('compounds.json'))


msg = "Hello world"
print(msg)
