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
    with open(filename, 'rb') as file:
        encoding = chardet.detect(file.read())['encoding']
        return encoding

def lstrip_bom(str_, bom=BOM_UTF8):
    if str_.startswith(bom):
        return str_[len(bom):]
    else:
        return str_

print(detect_encoding('schema.json'))
print(detect_encoding('compounds.json'))

json_data = json.load(codecs.open('compounds.json', 'r', 'UTF-8-SIG'))
print(json_data[0])
print(codecs.BOM_UTF8)

stripped_json_data = json.loads(lstrip_bom(open('compounds.json','rb').read()))
# print(stripped_json_data[0])

print(validate_json(stripped_json_data))

msg = "Hello world"
print(msg)
