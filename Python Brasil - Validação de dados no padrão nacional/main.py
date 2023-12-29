from model.Document import Document
from model.Phone import Phone
from model.Date import Date
from model.CepAccess import SearchAddress

cnpj = "35379838000112"
document = Document.create_document(cnpj)
print(document)

cpf = "01234567890"
document = Document.create_document(cpf)
print(document)

phone = "5549991234567"
phone = Phone(phone)
print(phone)

date = Date()
print(date.month())
print(date.day())
print(date)

cep = "89010000"
address = SearchAddress(cep)
print(address)
print(address.api_request())