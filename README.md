# Auto Test Generator com LangChain + OpenAI

Este projeto implementa um agente de IA que gera automaticamente testes unitários com `pytest` a partir de funções Python, utilizando LangChain e a API da OpenAI.

---

## Como funciona

1. O agente recebe um código Python como entrada.
2. Ele interpreta a lógica da função.
3. Gera um arquivo `test_<nome>.py` com testes de sucesso e falha.
4. Os testes podem ser executados com `pytest`.

---

# Como usar

## 1. Baixe as dependências 

pip install -r requirements.txt

## 2. Configure a sua chave da OpenAII
Crie um arquivo .env com base no .env.example:
OPENAI_API_KEY=sk-sua-chave-aqui

## 3. Execute o agente

python main.py

## 4. Rode os testes gerados

pytest test_soma.py

# Testes gerados

import pytest

def test_soma_sucesso():
    assert soma(2, 3) == 5

def test_soma_falha():
    with pytest.raises(TypeError):
        soma(2, "a")
