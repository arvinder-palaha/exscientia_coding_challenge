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
        self.table.field_names = [name[0] for name in self.headers]

    def _generate_link(self, id):
        link = '<a href="{}.html">assay results</a>'
        return link.format(id)

    def populate(self, data_list, preferred_id_field=0):
        for data in data_list:
            row_to_add = []
            id_for_link = data[self.headers[0][0]]
            print(id_for_link)
            for head in self.headers:
                if head[1] != 'array':
                    row_to_add.append(data[head[0]])
                else: # if array
                    if head[0] == 'assay_results':
                        row_to_add.append(self._generate_link(id_for_link))
                    else:
                        row_to_add.append(str(len(data[head[0]])))
            self.table.add_row(row_to_add)

    def get_string(self):
        return self.table.get_string()
    
# god function
def generate_html_report():
    """Created a tabulated report of the json data file
    contents as a html file"""
    pass
