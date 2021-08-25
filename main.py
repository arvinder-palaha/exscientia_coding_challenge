import json
from jsonschema import validate
import chardet
from codecs import BOM_UTF8
import codecs

import matplotlib.pyplot as plt
import numpy as np

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

def detect_encoding(filename):
    """Estimate encoding using chardet"""
    with open(filename, 'rb') as file:
        encoding = chardet.detect(file.read())['encoding']
        return encoding


stripped_json_data = get_json_data_from_file('data/compounds.json')

print(validate_json(stripped_json_data))

mol_weights = []
ALogP = []
num_rings = []

for compound in stripped_json_data:
    mol_weights.append(compound['molecular_weight'])
    ALogP.append(compound['ALogP'])
    num_rings.append(compound['num_rings'])

# print(num_rings)
area = [n*2 for n in num_rings]


fig, ax = plt.subplots()
ax.scatter(mol_weights, ALogP, s=area, c=num_rings)
ax.set_title('molecular weight Vs ALogP')
ax.set_xlabel('molecular weight')
ax.set_ylabel('ALogP')
ax.grid()
plt.show()

