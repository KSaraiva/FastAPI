class Conta:
    def __init__(self, account_id, saldo) -> None:
        self.id = account_id
        self.saldo = saldo

    def deposita(self, valor) -> None:
        self.saldo += valor

    def __pode_sacar(self, valor) -> bool:
        valor_total_disponivel = self.saldo
        return valor_total_disponivel >= valor

    def saca(self, valor) -> bool:
        if self.__pode_sacar(valor):
            self.saldo -= valor
            return True
        return False

    def transfere(self, valor, conta_destino: 'Conta') -> bool:
        if self.saca(valor):
            conta_destino.deposita(valor)
            return True
        return False
