import pytest
from requests import post
from json import loads

class TestAPI:
    def setup_method(self):
        self.url = 'http://127.0.0.1:8000'

    def test_APIstatus(self):
        response = post(self.url, json={"valor1": 1, "valor2": 2, "operacao": "adicao"})
        assert response.ok

    def test_APIresponse(self):
        response = post(self.url, json={"valor1": 1, "valor2": 2, "operacao": "adicao"})
        dict_ad = loads(response.text)
        resultado1 = dict_ad["resultado"]
        response = post(self.url, json={"valor1": 1, "valor2": 2, "operacao": "subtracao"})
        dict_sub = loads(response.text)
        resultado2 = dict_sub["resultado"]
        response = post(self.url, json={"valor1": 1, "valor2": 2, "operacao": "multiplicacao"})
        dict_mul = loads(response.text)
        resultado3 = dict_mul["resultado"]
        response = post(self.url, json={"valor1": 1, "valor2": 2, "operacao": "divisao"})
        dict_div = loads(response.text)
        resultado4 = dict_div["resultado"]
        assert resultado1 == 3
        assert resultado2 == -1
        assert resultado3 == 2
        assert resultado4 == 0.5
