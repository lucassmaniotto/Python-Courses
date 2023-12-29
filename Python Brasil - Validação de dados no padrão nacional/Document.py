from validate_docbr import CPF, CNPJ

class Document:
    @staticmethod
    def create_document(document):
        document = str(document)
        if len(document) == 11:
            return DocCpf(document)
        elif len(document) == 14:
            return DocCnpj(document)
        else:
            raise ValueError("Quantidade de dígitos inválida!")
        
class DocCpf:
    def __init__(self, document):
        document = str(document)
        if self.cpf_is_valid(document):
            self.cpf = document
        else:
            raise ValueError("CPF inválido!")

    def cpf_is_valid(self, document):
        validator = CPF()
        return validator.validate(document)
    
    def format_cpf(self):
        return CPF().mask(self.cpf)
    
    def __str__(self):
        return self.format_cpf()

class DocCnpj:
    def __init__(self, document):
        document = str(document)
        if self.cnpj_is_valid(document):
            self.cnpj = document
        else:
            raise ValueError("CNPJ inválido!")
    
    def cnpj_is_valid(self, document):
        validator = CNPJ()
        return validator.validate(document)
        
    def format_cnpj(self):
        return CNPJ().mask(self.cnpj)
    
    def __str__(self):
        return self.format_cnpj()