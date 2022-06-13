from simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def most_products_stocket_by_company(products):
        return products

    @classmethod
    def generate(cls, products):
        stock_by_company = cls.most_products_stocket_by_company(products)
        return stock_by_company
