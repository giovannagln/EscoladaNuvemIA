import requests

def consulta_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        if "erro" in dados:
            return "CEP invélido."
        return """
        CEP: {dados ["cep"]}
        Logradouro: {dados ["logradouro"]}
        Bairo: {dados ["bairro"]}
        Cidade: {dados ["localidade"]}
        Estado: {dados ["uf"]}
        """
    except requests.RequestException as e:
        return f"Erro na consulta{e}."
    

cep = int(input("Digite um CEP para consulta (apenas números): "))
print("Consultando CEP...")
resultado = consulta_cep(cep)
print(resultado)