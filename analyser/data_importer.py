import json
from jsonschema import validate
from codecs import BOM_UTF8

# TODO wrap this all in one function that calls the rest

def lstrip_bom(str_, bom=BOM_UTF8):
    """remove the beginning encoding chars
    if necessary"""
    if str_.startswith(bom):
        return str_[len(bom):]
    else:
        return str_

def get_json_data_from_file(filename):
    with open(filename, 'rb') as file:
        json_data = json.loads(lstrip_bom(file.read()))
    return json_data

def validate_json(json_data, schema_file='data/schema.json'):
    """Test json data against the schema"""
    execute_api_schema = get_json_data_from_file(schema_file)

    try:
        validate(instance=json_data, schema=execute_api_schema)
    except Exception as err:
        print(err)
        return False, err
    
    return True, "JSON data is valid"
