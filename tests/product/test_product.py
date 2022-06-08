from inventory_report.inventory.product import Product
from datetime import date


def test_cria_produto():
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

    assert product.id == 1
    assert product.nome_da_empresa == "Michael Produtos"
    assert product.nome_do_produto == "Ultrabook"
    assert product.data_de_fabricacao == today
    assert product.data_de_validade == "2030-06-08"
    assert product.numero_de_serie == "050507"
    assert product.instrucoes_de_armazenamento == "Abra e use"
