import json
from jsonschema import validate
from codecs import BOM_UTF8
from matplotlib.markers import MarkerStyle

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.colors as mcolors
from matplotlib import cm
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


json_data = get_json_data_from_file('data/compounds.json')

print(validate_json(json_data))

mol_weights = []
ALogP = []
num_rings = []

for compound in json_data:
    mol_weights.append(compound['molecular_weight'])
    ALogP.append(compound['ALogP'])
    num_rings.append(compound['num_rings'])

scale_num_rings = 10
area = [scale_num_rings*n for n in num_rings]
legend_cols = [scale_num_rings*n for n in set(num_rings)]
legend_cols_norm = mcolors.Normalize(vmin=min(legend_cols), vmax=max(legend_cols))
for n in legend_cols:
    print(legend_cols_norm(n))
viridis = cm.get_cmap('viridis', len(legend_cols))
fig, ax = plt.subplots()
ax.scatter(mol_weights, ALogP, s=area, c=num_rings, alpha=0.5)
ax.set_title('Molecular Weight vs ALogP')
ax.set_xlabel('molecular weight')
ax.set_ylabel('ALogP')
ax.grid()
legend_markers = []
for n in legend_cols:
    legend_markers.append(mlines.Line2D(
        [], [], alpha=0.5, color=viridis(legend_cols_norm(n)),
        marker='o', linestyle=None, linewidth=0, markersize=2*n/scale_num_rings,
        label=str(n/scale_num_rings)))
ax.legend(handles=legend_markers, title="number of rings")
plt.show()

