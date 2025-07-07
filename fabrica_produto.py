import exceptions
from interfaces.produto import Produto
from classes.produto import Cafe, CafeLatte, ChaVerde, Brownie

class FabricaProduto:
    def __init__(self):
        self.tipos_produto = {
            "cafe": Cafe,
            "cafe_latte": CafeLatte,
            "cha_verde": ChaVerde,
            "brownie": Brownie
        }

    def criar_produto(self, tipo: str) -> Produto:
        tipo = tipo.lower()
        if tipo  in self.tipos_produto:
            return self.tipos_produto[tipo]()
        else:
            raise exceptions.ProdutoCadastradoError(tipo)