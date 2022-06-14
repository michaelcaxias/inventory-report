import csv
import json
import xmltodict
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


class XMLReader:
    def read(self, path):
        with open(path) as file:
            products = xmltodict.parse(file.read())
            return products["dataset"]["record"]


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

        products = ""

        if file_extension_from_path == "csv":
            products = CSVReader.read(cls, path)
        if file_extension_from_path == "json":
            products = JSONReader.read(cls, path)
        if file_extension_from_path == "xml":
            products = XMLReader.read(cls, path)

        return cls.report_types[type].generate(products)
