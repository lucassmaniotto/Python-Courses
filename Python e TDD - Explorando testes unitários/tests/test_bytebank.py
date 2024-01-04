import datetime
from src.bytebank import Funcionario

class TestClass:
    def test_when_idade_received_date_of_birth_then_return_age(self):
        # Given
        entry = '01/01/2000'
        expected = datetime.date.today().year - 2000

        # When
        employee_test = Funcionario('Test', entry, 1000)
        result = employee_test.idade()

        # Then
        assert result == expected

    def test_when_sobrenome_received_Lucas_Carvalho_then_return_Carvalho(self):
        # Given
        entry = 'Lucas Carvalho        '
        expected = 'Carvalho'

        # When
        employee_test = Funcionario(entry, '01/01/2000', 1000)
        result = employee_test.sobrenome()

        # Then
        assert result == expected
