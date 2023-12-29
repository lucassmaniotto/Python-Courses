from Document import Document
from Phone import Phone
from Date import Date

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
