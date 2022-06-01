from typing import Union

from modelo.conta import Conta


def saldo(account_id, items):
    retorno_busca = busca_conta(account_id, items)
    if retorno_busca is not None:
        return retorno_busca.saldo
    else:
        return 0


def busca_conta(id_conta, items) -> Union[Conta, None]:
    for conta in items:
        if conta.id == id_conta:
            return conta
    return None
