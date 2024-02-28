def Calcula_Salario_Liquido(valHoraAula, aulasDadas, descInss):
    valAulas = valHoraAula * aulasDadas
    valDescontado = valAulas * (descInss / 100)
    valFinal = valAulas - valDescontado

    return round(valFinal, 2)

def Calculo_Desconto(ValorProduto):
    Desconto = ValorProduto * 0.09
    ValorProdutoDescontado = ValorProduto - Desconto

    return ValorProdutoDescontado

def calcular_conta_restaurante(valor_despesa):
    valor_despesa = float(valor_despesa)
    valor_gorjeta = valor_despesa * 0.1
    valor_total_conta = valor_despesa + valor_gorjeta
    return valor_total_conta, valor_gorjeta


def calcular_valor_promocional(valor_original, desconto):

  if not 0 <= desconto <= 1:
    raise ValueError("Desconto deve ser um valor entre 0 e 1.")

  valor_desconto = valor_original * desconto
  valor_final = valor_original - valor_desconto
  return valor_final