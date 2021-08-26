import pytest
import json
from analyser.data_importer import _get_json_data_from_file
from report.report_html import table_html

@pytest.fixture
def test_schema():
    return _get_json_data_from_file('tests/test_report/schema.json')

@pytest.fixture
def test_compounds():
    return _get_json_data_from_file('tests/test_report/test_compound.json')

@pytest.fixture
def exp_main_headers():
    return [['compound_id', 'integer'],
        ['smiles', 'string'],
        ['assay_results', 'array'],
    ]

@pytest.fixture
def exp_empty_table_str():
    string =  "+-------------+--------+---------------+\n"
    string += "| compound_id | smiles | assay_results |\n"
    string += "+-------------+--------+---------------+\n"
    string += "+-------------+--------+---------------+"
    return string

@pytest.fixture
def exp_filled_table():
    string =  "+-------------+----------------------------------------------------------+---------------+\n"
    string += "| compound_id |                          smiles                          | assay_results |\n"
    string += "+-------------+----------------------------------------------------------+---------------+\n"
    string += "|   1117973   |  Cc1nnc2[C@H](NC(=O)OCc3ccccc3)N=C(c4ccccc4)c5ccccc5n12  |      link     |\n"
    string += "|    694811   | CCNC(=O)C[C@@H]1N=C(c2ccc(Cl)cc2)c3cc(OC)ccc3n4c(C)nnc14 |      link     |\n"
    string += "+-------------+----------------------------------------------------------+---------------+"
    return string

def test_get_headers_from_schema_json(test_schema, exp_main_headers):
    test_table = table_html()
    test_table._column_headers(test_schema)
    table_headers = test_table.headers
    assert table_headers == exp_main_headers

def test_use_schema_as_argument(test_schema, exp_main_headers):
    test_table = table_html(test_schema)
    assert test_table.headers == exp_main_headers

def test_create_empty_table_with_headers(test_schema, exp_empty_table_str):
    test_table = table_html(test_schema)
    table_str = test_table.get_string()
    assert table_str == exp_empty_table_str

def test_create_filled_headed_table(test_schema, test_compounds, exp_filled_table):
    test_table = table_html(test_schema)
    test_table.populate(test_compounds)
    print(test_table.get_string())
    assert test_table.get_string() == exp_filled_table

