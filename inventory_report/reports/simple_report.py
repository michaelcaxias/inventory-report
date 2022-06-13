from collections import Counter
from datetime import date


class SimpleReport:
    def get_oldest_fabrication_date(self, products):
        return min([product["data_de_fabricacao"] for product in products])

    def get_next_expiration_date(self, products):
        filter_nexts_projects = filter(
            lambda product: product["data_de_validade"] > str(date.today()),
            products,
        )
        return min(
            [product["data_de_validade"] for product in filter_nexts_projects]
        )

    def get_company_more_products(self, products):
        return Counter(
            [product["nome_da_empresa"] for product in products]
        ).most_common(1)[0][0]

    @classmethod
    def generate(cls, products):
        oldest_fabrication_date = cls.get_oldest_fabrication_date(
          cls, products
          )
        next_expiration_date = cls.get_next_expiration_date(
          cls, products
          )
        company_with_more_products = cls.get_company_more_products(
          cls, products
          )

        return (
            f"Data de fabricação mais antiga: {oldest_fabrication_date}\n"
            f"Data de validade mais próxima: {next_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
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

simple_report = SimpleReport().generate(test_produts)
print(simple_report)
