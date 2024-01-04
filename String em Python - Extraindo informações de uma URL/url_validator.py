import re

url = 'www.bytebank.com.br/cambio'
url_pattern = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = url_pattern.match(url)

if not match:
    raise ValueError("A URL não é válida.")

print("A URL é válida")