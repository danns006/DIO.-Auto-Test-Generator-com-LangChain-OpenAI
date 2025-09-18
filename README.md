# Auto Test Generator com LangChain + OpenAI

Este projeto implementa um agente de IA que gera automaticamente testes unitários com `pytest` a partir de funções Python, utilizando LangChain e a API da OpenAI.

---

## Como funciona

1. O agente recebe um código Python como entrada.
2. Ele interpreta a lógica da função.
3. Gera um arquivo `test_<nome>.py` com testes de sucesso e falha.
4. Os testes podem ser executados com `pytest`.

---

## Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/auto-test-agent
cd auto-test-agent

