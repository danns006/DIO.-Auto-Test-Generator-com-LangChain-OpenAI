import os
from langchain.chat_models import ChatOpenAI

def gerar_testes(codigo):
    prompt = f"""
    Gere testes unitários usando pytest para o seguinte código Python:
    {codigo}
    Os testes devem incluir casos de sucesso e falha.
    """
    llm = ChatOpenAI(
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        model_name="gpt-3.5-turbo"
    )
    resposta = llm.invoke(prompt)
    return resposta.content

if __name__ == "__main__":
    with open("soma.py", "r") as f:
        codigo_soma = f.read()

    testes_soma = gerar_testes(codigo_soma)

    with open("test_soma.py", "w") as f:
        f.write(testes_soma)

    print("Testes gerados com sucesso!")
