import atividade
import pytest

funcao = atividade

class TesteAtividade():
    def teste_salarioLiquido(self):
        assert funcao.Calcula_Salario_Liquido(6.25, 160, 1.3) == 987
        assert funcao.Calcula_Salario_Liquido(20.5, 240, 1.7) == 4836.36
        assert funcao.Calcula_Salario_Liquido(13.9, 200, 6.48) == 2599.86


    def teste_valorProduto(self):
        assert funcao.Calculo_Desconto(100) == 91.00
        assert funcao.Calculo_Desconto(1500) == 1365.00
        assert funcao.Calculo_Desconto(60000) == 54600.00


    def test_calcular_conta_restaurante(self):

        test_cases = [
            (75.00, 82.50, 7.5),
            (125.00, 137.50, 12.5),
            (350.87, 385.96, 35.09),
        ]

        for valor_despesa, valor_total_esperado, valor_gorjeta_esperado in test_cases:
            valor_total_conta, valor_gorjeta = funcao.calcular_conta_restaurante(valor_despesa)
            assert valor_total_conta == pytest.approx(valor_total_esperado, abs=0.01)  # tolerancia
            assert valor_gorjeta == pytest.approx(valor_gorjeta_esperado, abs=0.01)  # tolerancia

    def test_calcular_valor_promocional(self):
        valor_original = 500.0
        desconto = 0.05
        valor_esperado = 475.0
        valor_calculado = funcao.calcular_valor_promocional(valor_original, desconto)
        assert valor_calculado == valor_esperado

        valor_original = 10500.0
        desconto = 0.1
        valor_esperado = 9450.0
        valor_calculado = funcao.calcular_valor_promocional(valor_original, desconto)
        assert valor_calculado == valor_esperado

        valor_original = 90.0
        desconto = 0.8
        valor_esperado = 18.0
        valor_calculado = funcao.calcular_valor_promocional(valor_original, desconto)
        assert valor_calculado == valor_esperado

        with pytest.raises(ValueError):
            funcao.calcular_valor_promocional(valor_original, -0.1)

        with pytest.raises(ValueError):
            funcao.calcular_valor_promocional(valor_original, 1.1)


if __name__ == "__main__":
    pytest.main()