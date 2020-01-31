import csv
import ast


class TableReader():

    def __init__(self, csv_filename):
        table = open(csv_filename, newline='')
        self.reader = csv.DictReader(table, delimiter=';')

    def read_item(self):
        for item in self.reader:
            evaluated_item = {}
            for key, value in item.items():
                try:
                    evaluated_item[key] = ast.literal_eval(value)
                except:
                    evaluated_item[key] = value
            yield evaluated_item

class TableWriter():

    def __init__(self, csv_filename, fieldnames) :
        table = open(csv_filename, 'w', newline='')
        self.writer = csv.DictWriter(table, fieldnames=fieldnames, delimiter=';')
        self.writer.writeheader()

    def write_item(self, item):
        self.writer.writerow(item)
        