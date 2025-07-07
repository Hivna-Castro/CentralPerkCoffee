from abc import ABC, abstractmethod

class Produto(ABC):
    @abstractmethod
    def __init__(self, nome: str, preco_base: float, preparo: str):
        self.nome = nome
        self.preco_base = preco_base
        self.preparo = preparo
