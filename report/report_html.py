from prettytable import PrettyTable

def _column_headers(schema):
    headers = []
    properties = schema['properties']
    for property in properties:
        prop_dict = properties[property]
        s_name = str(property)
        s_type = str(prop_dict['type'])
        headers.append([s_name, s_type])
    return headers


# god function
def generate_html_report():
    """Created a tabulated report of the json data file
    contents as a html file"""
    pass