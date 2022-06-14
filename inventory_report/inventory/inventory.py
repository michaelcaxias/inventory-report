import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

class CSV_reader:
    def read(path):
        with open(path) as file:
            file_data = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(file_data)


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
    data = ''
    if file_extension_from_path == "csv":
      data = CSV_reader.read(path)
    return cls.report_types[type].generate(data)
