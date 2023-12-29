from validate_docbr import CPF

class Cpf:
    def __init__(self, document):
        document = str(document)
        if self.cpf_is_valid(document):
            self.cpf = document
        else:
            raise ValueError("CPF inválido!")

    def cpf_is_valid(self, document):
        if len(document) == 11:
            validador = CPF()
            return validador.validate(document)
        else:
            raise ValueError("Quantidade de dígitos inválida!")
        
    def format_cpf(self):
        return CPF().mask(self.cpf)
    
    def __str__(self):
        return self.format_cpf()