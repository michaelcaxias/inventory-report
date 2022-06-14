import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class CSVReader:
    def read(self, path):
        with open(path) as file:
            products = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(products)


class JSONReader:
    def read(self, path):
        with open(path) as file:
            products = json.load(file)
            return products


class Inventory:
    report_types = {"simples": SimpleReport, "completo": CompleteReport}

    @classmethod
    def import_data(cls, path, type):
        """
        cls is the class
        path is the path to the file
        type is the type of data
        there are 2 types of data:
          - "simples"
          - "completo"
        """
        file_extension_from_path = path.split(".")[-1]

        file_reader = {
            "csv": CSVReader.read(cls, path),
            "json": JSONReader.read(cls, path),
        }

        products = file_reader[file_extension_from_path]

        return cls.report_types[type].generate(products)


test = Inventory.import_data("inventory_report/data/inventory.json", "simples")
