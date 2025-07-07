class ProdutoCadastradoError(Exception):
    def __init__(self, tipo: str):
        super().__init__(f"O tipo '{tipo}' de produto não foi cadastrado.")