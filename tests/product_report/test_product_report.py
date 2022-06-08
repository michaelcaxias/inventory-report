from inventory_report.inventory.product import Product
from datetime import date


def test_relatorio_produto():
    today = date.today()
    product = Product(
      id=1,
      nome_da_empresa="Michael Produtos",
      nome_do_produto="Ultrabook",
      data_de_fabricacao=today,
      data_de_validade="2030-06-08",
      numero_de_serie="050507",
      instrucoes_de_armazenamento="Abra e use"
    )

    expected_value = (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
    assert product.__repr__() == expected_value
