from classes.desconto import EstrategiaDesconto
from classes.notificador import Notificador

class Pedido:
    def __init__(self, desconto:EstrategiaDesconto):
        self.produtos = []
        self.notificadores = []
        self.desconto = desconto
    
    def set_desconto(self, desconto: EstrategiaDesconto):
        """Permite trocar a estratégia de desconto dinamicamente."""
        self.desconto = desconto
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def registrar_notificador(self, notificador: Notificador):
        self.notificadores.append(notificador)
    
    def notificar_observadores(self, mensagem):
        for notificador in self.notificadores:
            notificador.notificar(mensagem)

    def finalizar_pedido(self):
        total_bruto = sum(produto.preco_base for produto in self.produtos)
        total_com_desconto = self.desconto.aplicar_desconto(total_bruto)
        finalizacao = f"O pedido foi finalizado. Total com desconto: R${total_com_desconto:.2f}"
        self.notificar_observadores(finalizacao)
