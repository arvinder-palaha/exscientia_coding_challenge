import json
from jsonschema import validate
from codecs import BOM_UTF8

def _lstrip_bom(str_, bom=BOM_UTF8):
    """remove the beginning encoding chars if necessary"""
    if str_.startswith(bom):
        return str_[len(bom):]
    else:
        return str_

def _get_json_data_from_file(filename):
    with open(filename, 'rb') as file:
        json_data = json.loads(_lstrip_bom(file.read()))
    return json_data

def _validate_json(json_data, schema_file='data/schema.json'):
    """Test json data against the schema"""
    execute_api_schema = _get_json_data_from_file(schema_file)

    try:
        validate(instance=json_data, schema=execute_api_schema)
    except Exception as err:
        print(err)
        return False, err
    
    return True, "JSON data is valid"

def import_json(json_file, schema_file):
    """import json data validate against schema"""
    json_data = _get_json_data_from_file(json_file)
    valid, msg = _validate_json(json_data, schema_file=schema_file)
    if valid:
        return json_data
    else:
        print("Invalid JSON")
        return 0
