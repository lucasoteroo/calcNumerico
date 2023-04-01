import math


def funcao(x):
  #função da minha integral
    return math.exp(-x ** 2)


def integral_trapezio_repetida(f, a, b, n_subintervals):
    """
    Implementação da regra dos trapézios para aproximar a integral de uma função f no intervalo [a, b].
    n_subintervals é o número de subintervalos utilizados na aproximação.
    """

    h = (b - a) / n_subintervals  # tamanho de cada subintervalo

    x = []
    for i in range(n_subintervals + 1):
        point = a + i * h
        x.append(point)  # pontos x de cada subintervalo

    y= []   
    for x_i in x: #o loop "for" para calcular o valor de y correspondente a cada ponto x. 
      y_i = f(x_i)
      y.append(y_i)
 # valores de y correspondentes a cada ponto x

    # soma das áreas dos trapézios, O resultado da aproximação é armazenado na variável "integral". O cálculo é feito utilizando a fórmula:
    integral = (h / 2) * (y[0] + 2 * sum(y[1:n_subintervals]) + y[n_subintervals])
    #O primeiro termo, y[0], corresponde à altura do trapézio formado pelos pontos iniciais do intervalo [a,b].
    # O último termo, y[n_subintervals], corresponde à altura do trapézio formado pelos pontos finais do intervalo [a,b].
    return integral


# Definindo os parâmetros do problema
a = 0
b = 1
n_subintervals = 41 #número de retangulinhos

# Realizando o cálculo da integral
result = integral_trapezio_repetida(funcao, a, b, n_subintervals)

print("O resultado da integral da função math.exp(-x ** 2) ","é :",result)
