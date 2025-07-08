from fabrica_produto import FabricaProduto
from classes.desconto import DescontoClienteFrequente, DescontoPromocaoDia, DescontoCupomPersonalizado
from classes.pedido import Pedido
from classes.cliente import Cliente
from classes.notificador import NotificadorCliente, NotificadorCozinha, LoggerSistema
from exceptions import ProdutoCadastradoError

def processar_pedido(cliente, produtos):
    if cliente.frequente:
        desconto = DescontoClienteFrequente()
    else:
        desconto = DescontoPromocaoDia()
    pedido = Pedido(desconto)
    fabrica = FabricaProduto()
    try:
        for produto in produtos:
            pedido.adicionar_produto(fabrica.criar_produto(produto))
    except ProdutoCadastradoError as e:
        print(e)
    pedido.registrar_notificador(NotificadorCliente())
    pedido.registrar_notificador(NotificadorCozinha())
    pedido.registrar_notificador(LoggerSistema())
    print(f"--- Pedido do cliente {cliente.nome} ---")
    pedido.finalizar_pedido()

# Testando com clientes diferentes
cliente1 = Cliente("Ross", frequente=True)
cliente2 = Cliente("Monica", frequente=False)

processar_pedido(cliente1, ["cafe", "brownie"])
processar_pedido(cliente2, ["cafe", "brownie"])
