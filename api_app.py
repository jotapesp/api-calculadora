from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Annotated
import re

app = FastAPI()

class Resp(BaseModel):
     valor1: int
     valor2: int
     operacao: str

@app.post("/")
async def root(resp: Resp):
    try:
        output = 0
        if (re.findall(r'adi[cç][aã]o', resp.operacao) or (resp.operacao == 'soma')
         or resp.operacao == "+"):
            output = resp.valor1 + resp.valor2
        elif (re.findall(r'subtra[cç][aã]o', resp.operacao) or (resp.operacao == '-')):
            output = resp.valor1 - resp.valor2
        elif (re.findall(r'multiplica[cç][aã]o', resp.operacao) or (resp.operacao == '*')):
            output = resp.valor1 * resp.valor2
        elif (re.findall(r'divis[aã]o', resp.operacao) or (resp.operacao == '/')):
            output = resp.valor1 / resp.valor2
        return {"valor1": resp.valor1, "valor2": resp.valor2, "operacao": resp.operacao, "resultado": output}
    except ZeroDivisionError:
        raise HTTPException(status_code=404, detail="Não pode dividir por 0")
    except Exception as error:
        raise HTTPException(status_code=404, detail=f"{error}")
