import requests

cep = "832.60-000"

cep = cep.replace("-", "").replace(".", "").replace(" ", "")

if len(cep) == 8:
  print("Cep valido")
else:
    print("Cep invalido")
link = f'https://viacep.com.br/ws/{cep}/json/'
requisiçao = requests.get(link)
print(requisiçao)
dic_requisiçao = (requisiçao.json())
uf = dic_requisiçao['uf']
print(uf)
cidade = dic_requisiçao['localidade']
print(cidade)
bairro = dic_requisiçao['bairro']
print(bairro)
rua = dic_requisiçao['logradouro']
print(rua)
estado = dic_requisiçao['estado']
print(estado)
regiao = dic_requisiçao['regiao']
print(regiao)
ddd = dic_requisiçao['ddd']
print(ddd)
ibge = dic_requisiçao['ibge']
print(ibge)
