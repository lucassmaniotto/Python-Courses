url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

# Separando a base da URL dos parâmetros
url_params = url[url.find("?")+1:]
print(url_params)

# Buscando o valor de um parâmetro
search_param = "moedaDestino"
index_param = url_params.find(search_param)
index_value = index_param + len(search_param) + 1
end_index = url_params.find("&", index_value)

if end_index == -1:
    end_index = len(url_params)
value = url_params[index_value:end_index]

print(value)