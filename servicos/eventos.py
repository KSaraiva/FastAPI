from modelo.conta import Conta
from servicos.eventos_conta import busca_conta


def deposito(request, items):
    account_id = int(request['destination'])
    amount = request['amount']
    conta = busca_conta(account_id, items)
    if conta is not None:
        conta.deposita(amount)
        return {
            "destination": {
                "id": str(conta.id),
                "balance": conta.saldo
                    }
                }
    else:
        items.append(Conta(account_id, amount))
        return {
            "destination": {
                "id": str(account_id),
                "balance": amount
            }
        }


def saque(request, items):
    account_id = int(request['origin'])
    amount = request['amount']
    conta = busca_conta(account_id, items)
    if conta is not None:
        conta.saca(amount)
        return {
            "origin": {
                "id": str(conta.id),
                "balance": conta.saldo
            }
        }
    else:
        return 0


def transferencia(request, items):
    origin = int(request['origin'])
    amount = request['amount']
    destination = int(request['destination'])
    conta_origem = busca_conta(origin, items)
    if conta_origem is not None:
        if busca_conta(destination, items) is None:
            items.append(Conta(destination, 0))
        conta_destino = busca_conta(destination, items)
        conta_origem.transfere(amount, conta_destino)
        return {
            "origin": {
                "id": str(conta_origem.id),
                "balance": conta_origem.saldo
            },
            "destination": {
                "id": str(conta_destino.id),
                "balance": conta_destino.saldo
            }
        }
    else:
        return 0
