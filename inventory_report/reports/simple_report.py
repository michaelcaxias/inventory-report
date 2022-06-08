class SimpleReport:
    def get_oldest_fabrication_date(self, products):
        return min([product["data_de_fabricacao"] for product in products])

    def generate(self, dict):
        oldest_fabrication_date = self.get_oldest_fabrication_date(dict)
        next_expiration_date = ""
        company_with_more_products = ""

        return f""""
          Data de fabricação mais antiga: {oldest_fabrication_date}
          Data de validade mais próxima: {next_expiration_date}
          Empresa com mais produtos: {company_with_more_products}
        """
