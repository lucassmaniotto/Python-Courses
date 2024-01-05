from src.bytebank import Funcionario
import datetime

def test_age():
    funcionario = Funcionario('João Bragança', '05/02/2000', 100000)
    print(f'Testando idade: {funcionario.idade()}')

    funcionario.decrescimo_salario()
    print(f'Testando decrescimo salário: {funcionario.salario}')

    funcionario1 = Funcionario('Ana Mar' , '04/10/2000', 10000)
    print(f'Testando calculo de bonus: {funcionario1.calcular_bonus()}')

test_age()