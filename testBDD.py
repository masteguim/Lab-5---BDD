from BDD import Calculadora

def test_soma():
    # DADO
    calc = Calculadora()

    # quando
    resultado = calc.somar(2, 3)

    # ENTAO
    assert resultado == 5