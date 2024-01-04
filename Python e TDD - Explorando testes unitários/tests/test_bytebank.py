import datetime, pytest
from src.bytebank import Funcionario
from pytest import mark

class TestClass:
    @mark.idade
    def test_when_idade_received_date_of_birth_then_return_age(self):
        # Given
        entry = '01/01/2000'
        expected = datetime.date.today().year - 2000

        # When
        employee_test = Funcionario('Test', entry, 1000)
        result = employee_test.idade()

        # Then
        assert result == expected

    @mark.sobrenome
    def test_when_sobrenome_received_Lucas_Carvalho_then_return_Carvalho(self):
        # Given
        entry = 'Lucas Carvalho        '
        expected = 'Carvalho'

        # When
        employee_test = Funcionario(entry, '01/01/2000', 1000)
        result = employee_test.sobrenome()

        # Then
        assert result == expected

    @mark.decrescimo_salario
    def test_when_decrescimo_salario_received_100000_then_return_90000(self):
        # Given
        entry_salary = 100000
        entry_name = "João Bragança"
        expected = 90000

        # When
        employee_test = Funcionario(entry_name, '01/01/2000', entry_salary)
        employee_test.decrescimo_salario()
        result = employee_test.salario

        # Then
        assert result == expected

    @mark.decrescimo_salario
    def test_when_decrescimo_salario_received_10000_then_return_10000(self):
        # Given
        entry_salary = 10000
        entry_name = "João Bragança"
        expected = 10000

        # When
        employee_test = Funcionario(entry_name, '01/01/2000', entry_salary)
        employee_test.decrescimo_salario()
        result = employee_test.salario

        # Then
        assert result == expected

    @mark.decrescimo_salario
    def test_when_decrescimo_salario_received_100000_then_and_not_a_director_return_100000(self):
        # Given
        entry_salary = 100000
        entry_name = "João Silva"
        expected = 100000

        # When
        employee_test = Funcionario(entry_name, '01/01/2000', entry_salary)
        employee_test.decrescimo_salario()
        result = employee_test.salario

        # Then
        assert result == expected

    @mark.calcular_bonus
    def test_when_calcular_bonus_received_1000_then_return_100(self):
        # Given
        entry = 1000
        expected = 100

        # When
        employee_test = Funcionario('test', '01/01/2000', entry)
        result = employee_test.calcular_bonus()

        # Then
        assert result == expected

    @mark.calcular_bonus
    def test_when_calcular_bonus_received_100000_then_return_exception(self):
        with pytest.raises(Exception):
            # Given
            entry = 100000

            # When
            employee_test = Funcionario('test', '01/01/2000', entry)
            result = employee_test.calcular_bonus()

            # Then
            assert result