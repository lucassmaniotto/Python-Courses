from Document import Document

cnpj = "35379838000112"
document = Document.create_document(cnpj)
print(document)

cpf = "01234567890"
document = Document.create_document(cpf)
print(document)
