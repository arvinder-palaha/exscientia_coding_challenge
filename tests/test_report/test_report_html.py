import pytest
import json
from analyser.data_importer import _get_json_data_from_file
from report.report_html import table_html

@pytest.fixture
def test_schema():
    return _get_json_data_from_file('tests/test_report/schema.json')

def test_get_headers_from_schema_json(test_schema):
    test_table = table_html()
    test_table._column_headers(test_schema)
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

# def test_use_schema_as_argument

# def test_create_empty_table_with_headers(test_schema):
#     test_table = report_html()
#     test_table._column_headers(test_schema)
    


