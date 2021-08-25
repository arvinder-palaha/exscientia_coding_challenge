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

with open('compounds.json','r') as file:
    json_data = file.read()
    result, msg = validate_json(json_data)
    print(result, msg)



msg = "Hello world"
print(msg)
