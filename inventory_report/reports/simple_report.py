class SimpleReport:
    def generate(self, dict):
        oldest_fabrication_date = ''
        next_expiration_date = ''
        company_with_more_products = ''

        return f""""
          Data de fabricação mais antiga: {oldest_fabrication_date}
          Data de validade mais próxima: {next_expiration_date}
          Empresa com mais produtos: {company_with_more_products}
        """
