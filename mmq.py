import math
import numpy as np
import matplotlib.pyplot as plt


def mmq(g_1, g_2, x, y): # Define a função que implementa o método dos mínimos quadrados

    # Inicializa os valores dos coeficientes a_1 e a_2
    a_1 = 0
    a_2 = 0

# Calcula os elementos da matriz G
    G_11 = np.dot(g_1(x), g_1(x))
    G_12 = np.dot(g_1(x), g_2(x))
    G_21 = np.dot(g_2(x), g_1(x))
    G_22 = np.dot(g_2(x), g_2(x))

    G = [[G_11, G_12], [G_21, G_22]]

# Calcula os elementos do vetor b
    b_1 = np.dot(y, g_1(x))
    b_2 = np.dot(y, g_2(x))
    b = [b_1, b_2]

# Resolve o sistema linear para obter os valores dos coeficientes a_1 e a_2
    a = np.linalg.solve(G, b)

    a_1 = a[0]
    a_2 = a[1]

# Retorna os coeficientes a_1 e a_2
    return a_1, a_2
    
#Define as funções g_1, g_2 e g_3

def g_1(r):
    return np.ones(len(r))


def g_2(r):
    return np.sqrt(r)

def g_3(r):
    return np.log(r)


#Define os valores de x e y
x = np.array([1, 1.5, 2, 2.5, 3])
y = np.array([1.6, 5.6, 6, 7.1, 7])

#Usa o método dos mínimos quadrados para obter os coeficientes a_1 e a_2 da função phi(z)
a_1, a_2 = mmq(g_1, g_2, x, y)

#Usa o método dos mínimos quadrados para obter os coeficientes a_3 e a_4 da função phii(z)
a_3, a_4 = mmq(g_1, g_3, x, y)


#Define as funções phi(z) e phii(z)
def phi(z): 
    return a_1 + a_2 * g_2(z)

def phii(z): 
    return a_3 + a_4 * g_3(z)

#Define os valores de x_r e x_t para os gráficos
x_r = np.linspace(1, 3, 100)
x_t = np.linspace(1, 3, 100)

#Calcula os valores de y_r e y_t para os gráficos
y_r = phi(x_r)
y_t = phii(x_t)

#Plota o gráfico com os pontos (x,y) e as funções phi(z) e phii(z)
plt.plot(x, y, 'o')
plt.plot(x_r, y_r, label='sqrt(x)')
plt.plot(x_t, y_t, label='ln(x)')
plt.show

# Cálculo do erro quadrático geral

# Calcule o erro quadrático geral da seguinte maneira:
'''
Inicialize a variável erro =0 
faça um loop do tipo for de i = 0 até n (não incluindo n)
em que n é o tamanho do vetor x (ou y, eles devem ter o mesmo tamanho)
dentro do loop acumule o erro quadrático fazendo erro+= (y[i] - phi(x[i]))**2
imprima o erro obtido após o loop
'''
erro_sqrt=0
erro_ln =0

for i in range(len(x)):
  erro_sqrt+= (y[i] - phi(x[i]))**2
print("erro da função sqrt(x) é : ",erro_sqrt)


for i in range(len(x)):
  erro_ln+= (y[i] - phii(x[i]))**2
print("erro da função ln(x) é : ",erro_ln)
