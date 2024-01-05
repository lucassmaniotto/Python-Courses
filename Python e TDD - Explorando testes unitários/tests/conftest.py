def pytest_configure(config):
    config.addinivalue_line(
        "markers", "nome: mark test to nome"
    )

    config.addinivalue_line(
        "markers", "idade: mark test to idade"
    )

    config.addinivalue_line(
        "markers", "sobrenome: mark test to sobrenome"
    )
    
    config.addinivalue_line(
        "markers", "decrescimo_salario: mark test to decrescimo_salario"
    )

    config.addinivalue_line(
        "markers", "calcular_bonus: mark test to calcular_bonus"
    )
