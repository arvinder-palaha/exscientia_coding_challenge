import pytest
import json
from analyser.data_importer import _get_json_data_from_file
from report.report_html import _column_headers

def test_get_headers_from_schema_json():
    schema = _get_json_data_from_file('tests/test_report/schema.json')
    table_headers = _column_headers(schema)
    expected_headers = [['compound_id', 'integer'],
        ['smiles', 'string'],
        ['molecular_weight', 'number'],
        ['ALogP', 'number'],
        ['molecular_formula', 'string'],
        ['num_rings', 'number'],
        ['image', 'string'],
        ['assay_results', 'array'],
    ]
    assert table_headers == expected_headers
