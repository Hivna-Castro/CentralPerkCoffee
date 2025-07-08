from abc import ABC, abstractmethod

class EstrategiaDesconto(ABC):
    @abstractmethod
    def aplicar_desconto(self, preco_base: float) -> float:
        pass

class DescontoClienteFrequente(EstrategiaDesconto):
    def aplicar_desconto(self, preco_base) -> float:
        return preco_base - 2.00
    
class DescontoPromocaoDia(EstrategiaDesconto):
    def aplicar_desconto(self, preco_base) -> float:
        return preco_base * 0.90

class DescontoCupomPersonalizado(EstrategiaDesconto):
    def __init__(self, porcentagem_desconto: float):
        self.porcentagem_desconto = porcentagem_desconto
    def aplicar_desconto(self, preco_base):
        return preco_base * (1 - self.porcentagem_desconto / 100)
