from fabrica_produto import FabricaProduto
from exceptions import ProdutoCadastradoError

def main():
    fabrica = FabricaProduto()

    produto = fabrica.criar_produto("cafe_latte")
    print(f"Produto: {produto.nome}, R${produto.preco_base}, {produto.preparo}")

if __name__ == "__main__":
    main()