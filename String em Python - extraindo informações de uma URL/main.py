from url_extractor import URLExtractor

url_extractor = URLExtractor("https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")

print(url_extractor.get_base_url())
print(url_extractor.get_url_params())
print(url_extractor.get_param_value("quantidade"))
print(url_extractor.get_param_value("moedaOrigem"))
print(url_extractor.get_param_value("moedaDestino"))

print (f"O tamanho da URL é: {len(url_extractor)}")
print(url_extractor)

url_extractor_2 = URLExtractor("https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")

print(url_extractor == url_extractor_2)