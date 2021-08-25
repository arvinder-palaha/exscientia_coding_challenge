import json
from jsonschema import validate
import chardet
from codecs import BOM_UTF8
import codecs

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
    """Estimate encoding using chardet"""
    with open(filename, 'rb') as file:
        encoding = chardet.detect(file.read())['encoding']
        return encoding

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

# print(detect_encoding('schema.json'))
# print(detect_encoding('compounds.json'))

stripped_json_data = get_json_data_from_file('compounds.json')

print(validate_json(stripped_json_data))


