from analyser.data_importer import import_json, _get_json_data_from_file
from analyser.plotting import scatter_plot
from report.report_html import *
import argparse
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument('json_file', type=str)
parser.add_argument('schema_file', type=str)
parser.add_argument('--plot', action="store_true", help='plot molecular weight vs ALogP')
parser.add_argument('--report', action="store_true", help='create report of compounds results as build/index.html')
arguments = parser.parse_args()

if not os.path.exists(arguments.json_file):
    print('no such file:', arguments.json_file)
    sys.exit()

if not os.path.exists(arguments.schema_file):
    print('no such file:', arguments.schema_file)
    sys.exit()

json_data = import_json(json_file=arguments.json_file,schema_file=arguments.schema_file)
print("json data validated against schema")

if arguments.plot:
    mol_weights = []
    ALogP = []
    num_rings = []

    for compound in json_data:
        mol_weights.append(compound['molecular_weight'])
        ALogP.append(compound['ALogP'])
        num_rings.append(compound['num_rings'])

    scatter_plot(mol_weights, ALogP, num_rings, showplot=True, 
        title="Molecular Weight vs ALogP",
        xlabel='molecular weight',
        ylabel='ALogP',
        legend_title='number of rings')

if arguments.report:
    schema = _get_json_data_from_file(arguments.schema_file)
    generate_html_report(json_data, schema, image_dir='data/images')
    print('html report generated')

