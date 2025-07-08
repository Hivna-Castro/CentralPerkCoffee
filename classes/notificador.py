from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def notificar(self, mensagem):
        print(f"Notificação: {mensagem}")

class NotificadorCliente(Notificador):
    def notificar(self, mensagem):
        print(f"Notificação para o cliente: {mensagem}")

class NotificadorCozinha(Notificador):
    def notificar(self, mensagem):
        print(f"Notificação para a cozinha: {mensagem}")

class LoggerSistema(Notificador):
    def notificar(self, mensagem):
        print(f"Log do sistema: {mensagem}")