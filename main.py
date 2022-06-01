import json
from typing import List
from fastapi import FastAPI, Request, status, Response

from modelo.conta import Conta
from servicos.eventos import deposito, saque, transferencia
from servicos.eventos_conta import saldo

app = FastAPI()
items: List[Conta] = []


@app.post("/reset")
def reset():
    del items[0:]
    if len(items) == 0:
        return Response(
            content="OK",
            status_code=status.HTTP_200_OK,
            media_type="text/plain")
    else:
        return Response(content="",
                        status_code=status.HTTP_404_NOT_FOUND)


@app.get("/balance")
def read_item(account_id: int, response: Response):
    response.body = saldo(account_id, items)
    if not str(response.body) == "0":
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
    return response.body


@app.post('/event')
async def post_item(request: Request, response: Response):
    json_request = json.loads(json.dumps(await request.json()))
    if json_request['type'] == "deposit":
        response.body = deposito(json_request, items)
        if not str(response.body) == "0":
            response.status_code = status.HTTP_201_CREATED
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
    elif json_request['type'] == "withdraw":
        response.body = saque(json_request, items)
        if not str(response.body) == "0":
            response.status_code = status.HTTP_201_CREATED
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
    elif json_request['type'] == "transfer":
        response.body = transferencia(json_request, items)
        if not str(response.body) == "0":
            response.status_code = status.HTTP_201_CREATED
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
    return response.body
