from prettytable import PrettyTable
import html
import os

class table_html:
    def __init__(self, schema=None, image_dir=None):
        self.table = PrettyTable()
        self.headers = []
        if schema is not None:
            self._column_headers(schema)
        self._global_format_opts()
    
    def _global_format_opts(self):
        self.table.border = True
        self.table.format = True        

    def _column_headers(self, schema):
        properties = schema['properties']
        for property in properties:
            prop_dict = properties[property]
            s_name = str(property)
            s_type = str(prop_dict['type'])
            self.headers.append([s_name, s_type])
        self.table.field_names = [name[0] for name in self.headers]

    def _generate_link(self, id):

        link = '<a href="results/{}.html">assay results</a>'
        return link.format(id)

    def populate(self, data_list, preferred_id_field=0):
        for data in data_list:
            row_to_add = []
            id_for_link = data[self.headers[0][0]]
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

    def get_html(self):
        return html.unescape(self.table.get_html_string())
    
# god function
def generate_html_report(json_data, schema, image_dir=None):
    """Created a tabulated report of the json data file
    contents as a html file"""

    # main pass/table
    toptab = table_html(schema, image_dir=image_dir)
    toptab.table.border = True
    toptab.table.format = True
    toptab.populate(json_data)

    # create build dir if doesn't exist already
    if not os.path.isdir('build'):
        os.mkdir('build')

    # write table html to file
    with open('build/index.html', 'w') as f:
        f.write(toptab.get_html())

    # if any arrays found in header...
    for header in toptab.headers:
        if header[0] == 'assay_results':
            if not os.path.isdir('build/results'):
                os.mkdir('build/results')
            # loop pass for each set of results
            for compound in json_data:
                res_schema = schema['properties'][header[0]]
                res_data = compound[header[0]]
                results_tab = table_html(res_schema)
                results_tab.populate(res_data)
                c_id = compound['compound_id']
                with open('build/results/{}.html'.format(c_id), 'w') as f:
                    f.write(results_tab.get_html())


    
