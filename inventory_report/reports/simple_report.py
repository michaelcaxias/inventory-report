from datetime import date


class SimpleReport:
    def get_oldest_fabrication_date(self, products):
        return min([product["data_de_fabricacao"] for product in products])

    def get_next_expiration_date(self, products):
        filter_nexts_projects = filter(lambda product: product["data_de_validade"] > str(date.today()), products)
        return min(product["data_de_validade"] for product in filter_nexts_projects)


    def generate(self, products):
        oldest_fabrication_date = self.get_oldest_fabrication_date(products)
        next_expiration_date = ""
        company_with_more_products = ""

        return f""""
          Data de fabricação mais antiga: {oldest_fabrication_date}
          Data de validade mais próxima: {next_expiration_date}
          Empresa com mais produtos: {company_with_more_products}
        """

test_produts =    [
     {
       "id": 1,
       "nome_do_produto": "CADEIRA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2022-04-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48",
       "instrucoes_de_armazenamento": "Conservar em local fresco"
     }
   ]

simple_report = SimpleReport().get_next_expiration_date(test_produts)
print(simple_report)
