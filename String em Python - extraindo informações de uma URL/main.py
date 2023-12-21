from UrlExtractor import URLExtractor

url_extractor = URLExtractor("https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")

print(url_extractor.get_base_url())
print(url_extractor.get_url_params())
print(url_extractor.get_param_value("quantidade"))
print(url_extractor.get_param_value("moedaOrigem"))
print(url_extractor.get_param_value("moedaDestino"))