from interfaces.produto import Produto

class Cafe(Produto):
    def __init__(self):
        super().__init__(nome="Café", preco_base=2.0, preparo="Café coado com água quente sobre pó de café em filtro")

class CafeLatte(Produto):
    def __init__(self):
        super().__init__(nome="Café Latte", preco_base=4.0, preparo="Espresso com leite vaporizado e pouca espuma.")

class ChaVerde(Produto):
    def __init__(self):
        super().__init__(nome="Cha Verde", preco_base=4.0, preparo="Infusão de folhas de chá verde em água quente")

class Brownie(Produto):
    def __init__(self):
        super().__init__(nome="Cha Verde", preco_base=4.0, preparo="Bolo de chocolate sem fermento, denso e úmido")