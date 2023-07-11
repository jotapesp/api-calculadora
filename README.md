# API de Calculadora

(PT-BR)
Essa é uma API que faz as operações matemáticas básicas (adição, subtração, multiplicação e divisão) dados 2 números inteiros.

### Feito com

[![Python](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)](https://docs.python.org/3/)
[![FastAPI](https://img.shields.io/badge/FastAPI-000?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)

### Instalação

- `pip install -r requirements.txt`

<p>O arquivo requirements.txt vem no repositório e vai instalar todas as dependências da aplicação.</p>

### Como usar

(PT-BR)
<p>Para rodar o programa, abra o terminal e use o comando</p>

`uvicorn api_app:app --reload` .

#### Obtendo resultado das operações

<div>Após rodar o comando inicial, a URL a ser utilizada nos _requests_ será</div>`http://127.0.0.1:8000`<div>. A API aceita apenas _requests_ no método _POST_ e os valores devem ser passados em uma variável json, por exemplo:</div>

 - `resp = post("http://127.0.0.1:8000", json={"valor1": int, "valor2": int, "operacao": "nome_operacao"})`

<p>As operações aceitas são:</p>

 - Adição (substituia nome_operação por `adicao`, `adição`, `soma` ou `+`)
 - Subtração (substituia nome_operação por `subtracao`, `subtração` ou `-`)
 - Multiplicação (substituia nome_operação por `multiplicacao`, `multiplicação` ou `*`)
 - Divisão (substituia nome_operação por `divisao`, `divisão` ou `/`)

<p>As operações serão sempre realizadas respeitando a ordem `valor1` e `valor2`, ou seja, adição: `valor1 + valor2`, ou divisão: `valor1 / valor2`.
O resultado pode ser carregado em uma variável utilizando a função `loads` da biblioteca `json`, e vem no formato</p>

```python
{
 "valor1": valor1 int,
 "valor2": valor2 int,
 "operacao": operacao str,
 "resultado": resultado int
}
```

### Documentação

- [`documentation.html`](https://github.com/jotapesp/api-calculadora/blob/main/requirements.txt) ou
- `http://127.0.0.1:8000/docs`
