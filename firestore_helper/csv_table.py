import csv


class TableReader():

    def __init__(self, csv_filename):
        table = open(csv_filename, newline='')
        self.reader = csv.DictReader(table)

    def read_item(self):
        for item in self.reader:
            yield item

class TableWriter():

    def __init__(self, csv_filename, fieldnames) :
        table = open(csv_filename, 'w', newline='')
        self.writer = csv.DictWriter(table, fieldnames=fieldnames)
        self.writer.writeheader()

    def write_item(self, item):
        self.writer.writerow(item)
        