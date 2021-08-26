import pytest
import json
from analyser.data_importer import _get_json_data_from_file
from report.report_html import report_html

def test_get_headers_from_schema_json():
    schema = _get_json_data_from_file('tests/test_report/schema.json')
    test_table = report_html()
    test_table._column_headers(schema)
    table_headers = test_table.headers
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


