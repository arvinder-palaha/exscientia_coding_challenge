from prettytable import PrettyTable

class table_html:
    def __init__(self, schema=None):
        self.table = PrettyTable()
        self.headers = []
        if schema is not None:
            self._column_headers(schema)

    def _column_headers(self, schema):
        properties = schema['properties']
        for property in properties:
            prop_dict = properties[property]
            s_name = str(property)
            s_type = str(prop_dict['type'])
            self.headers.append([s_name, s_type])
    
    # def



# god function
def generate_html_report():
    """Created a tabulated report of the json data file
    contents as a html file"""
    pass
