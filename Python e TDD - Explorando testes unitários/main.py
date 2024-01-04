from src.bytebank import Funcionario

def test_age():
    funcionario = Funcionario('João', '13/03/2000', 2000)
    print(f'Testando idade: {funcionario.idade()}')

test_age()