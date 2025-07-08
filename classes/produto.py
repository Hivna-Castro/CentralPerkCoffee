from abc import ABC, abstractmethod

class Produto(ABC):
    @abstractmethod
    def __init__(self, nome: str, preco_base: float, preparo: str):
        self.nome = nome
        self.preco_base = preco_base
        self.preparo = preparo

class Cafe(Produto):
    def __init__(self):
        super().__init__(nome="Café", preco_base=5.0, preparo="Café coado com água quente sobre pó de café em filtro")

class CafeLatte(Produto):
    def __init__(self):
        super().__init__(nome="Café Latte", preco_base=6.0, preparo="Espresso com leite vaporizado e pouca espuma.")

class ChaVerde(Produto):
    def __init__(self):
        super().__init__(nome="Cha Verde", preco_base=5.0, preparo="Infusão de folhas de chá verde em água quente")

class Brownie(Produto):
    def __init__(self):
        super().__init__(nome="Brownie", preco_base=8.0, preparo="Bolo de chocolate sem fermento, denso e úmido")