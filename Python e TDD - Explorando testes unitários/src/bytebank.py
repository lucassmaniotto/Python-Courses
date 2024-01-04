from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nascimento = self._data_nascimento.split('/')
        ano_nascimento = int(data_nascimento[-1])
        mes_nascimento = int(data_nascimento[1])
        dia_nascimento = int(data_nascimento[0])
        
        data_atual = date.today()
        ano_atual = data_atual.year
        mes_atual = data_atual.month
        dia_atual = data_atual.day
        idade = ano_atual - ano_nascimento

        if mes_atual < mes_nascimento:
            idade -= 1
        elif mes_atual == mes_nascimento and dia_atual < dia_nascimento:
            idade -= 1
        return idade
    
    def sobrenome(self):
        nome_completo = self._nome.strip()
        sobrenome = nome_completo.split(' ')[-1]
        return sobrenome

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception(f'Bonus não pode ser maior que R$ 1000, o salário máximo é R$ 10000 | Salário informado: {self._salario}')
        return valor
    
    def _eh_diretor(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return self.salario >= 100000 and (self.sobrenome() in sobrenomes)
    
    def decrescimo_salario(self):
        if self._eh_diretor():
            self._salario = self._salario * 0.9

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'