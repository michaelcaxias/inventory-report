from typing import Counter
from simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def most_products_stocket_by_company(products):
        return (
          Counter([product["nome_da_empresa"] for product in products])
          .items()
        )

    @classmethod
    def generate(cls, products):
        stock_by_company = cls.most_products_stocket_by_company(products)
        company_name_and_stock = ""
        for company in stock_by_company:
            company_name_and_stock += f'- {company[0]}: {company[1]}\n'

        return (
          'Produtos estocados por empresa: \n'
          f'{company_name_and_stock}'
        )


test_produts = [
    {
        "id": 1,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-04-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    }
]

simple_report = CompleteReport().generate(test_produts)
print(simple_report)
