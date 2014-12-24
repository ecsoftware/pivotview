# This File handled different dynamic groups in pivot
# Normal Grouping : $ pivot.py -by Gender -by Location 
# Grouping in HTML format : $ pivot.py -by Gender -by Location -o html
# Grouping in CSV format : $ pivot.py -by Gender -by Location -o csv

import sys

class PivotView(object):
    def __init__(self, *args):
        self.args = args
        self.header_keys, self.output_keys = self.manage_args()
        self.split_data = lambda data: str(data.strip()).split("\t")
        self.filter_data = []
        with open('data.txt') as table_data:
            self.table_content = list(table_data)
            self.table_keys = self.get_header()
            for row in self.table_content:
                if row.strip() == "#END":
                    break
                else:
                    filter_row = self.get_filter_data(row)
                    self.filter_data.append(filter_row)

        self.valid_group = self.get_valid_group()

        if self.output_keys and "html" in self.output_keys:
            self.html_format_data()
        else:
            self.format_data()

    def manage_args(self):
        """
        Manage user arguments
        """
        header_keys = []
        output_keys = []
        for arg_item in self.args[0]:
            if arg_item[0] == "-by":
                header_keys.append(arg_item[1])
            if arg_item[0] == "-o":
                output_keys.append(arg_item[1])
        return header_keys, output_keys

    def get_header(self):
        """
        Capture the header data from  data table.
            ex: $ pivot.py -by Gender -by Location
            Here 'Gender' and 'Locations' are user expecting headers 
        """
        header_data = self.table_content.pop(0)
        header_keys = self.split_data(header_data)
        return header_keys

    def get_filter_data(self, row):
        """
        Group a dict with valid header keys.
            ex: $ pivot.py -by Gender -by Location
            Here 'Gender' and 'Locations' are user expecting header keys 
        """
        table_row = self.split_data(row)
        row_dict = dict(zip(self.table_keys, table_row))
        filter_data = {key: row_dict[key] for key in self.header_keys if key in row_dict}
        return filter_data

    def get_valid_group(self):
        """
        Remove the duplicate data and get the count of the data.
        """
        distinct_data = [dict(t) for t in set([tuple(d.items()) for d in self.filter_data])]
        for data in distinct_data:
            data["Count"] = self.filter_data.count(data)
        return distinct_data

    def format_data(self):
        """
        Formatting data only for CSV and Normal group 
        ex: $ pivot.py -by Gender -by Location -o csv
           or
        ex: $ pivot.py -by Gender -by Location
        """
        self.header_keys.append("Count")
        partition_data = "\t"
        if self.output_keys and "csv" in self.output_keys:
            partition_data = "," # for CSV conversion
            
        header = ""
        for key in self.header_keys:
            header += str(key) + partition_data
        else:
            header += "\n"

        rows = ""
        for valid_data in self.valid_group:
            for key in self.header_keys:
                rows += str(valid_data.get(key, "undefined")) + partition_data
            else:
                rows += "\n"
        print header + rows

    def html_format_data(self):
        """
        Formatting data only for CSV and Normal group 
        ex: $ pivot.py -by Gender -by Location -o html
        """
        self.header_keys.append("Count")
        table_tag = "<table>\n%s</table>"
        html_head = "<tr> \n"
        for key in self.header_keys:
            html_head += ("\t <td> %s </td>" %key) + "\n"
        else:
            html_head += "</tr> \n"

        rows = ""
        for valid_data in self.valid_group:
            rows += "<tr> \n"
            for key in self.header_keys:
                rows += ("\t<td> %s </td>" % str(valid_data.get(key, "undefined"))) + "\n"
            else:
                rows += "</tr> \n" 

        html_data = table_tag %(html_head + rows)
        print html_data

if __name__ == "__main__":
   args = sys.argv[1:]
   args_key = args[::2]
   args_value = args[1::2]
   filter_args = zip(args_key, args_value)
   PivotView(filter_args)
