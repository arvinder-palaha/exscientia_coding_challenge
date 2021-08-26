from prettytable import PrettyTable

class report_html:
    def __init__(self):
        self.table = PrettyTable()
        self.headers = []

    def _column_headers(self, schema):
        properties = schema['properties']
        for property in properties:
            prop_dict = properties[property]
            s_name = str(property)
            s_type = str(prop_dict['type'])
            self.headers.append([s_name, s_type])



# god function
def generate_html_report():
    """Created a tabulated report of the json data file
    contents as a html file"""
    pass