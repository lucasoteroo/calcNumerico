#MÉTODO do ponto fixo
import math

def f(x):
  return math.exp(x) - 2 * x -1

#Função phi(x)
def phi(x):
  return (1/2)*math.exp(x)

#PRECISÃO DE 4 CASAS DECIMAIS
erro_max=0.0001

# X inicial
x_0=0.6
x= x_0

cont=0
while math.fabs(f(x))>erro_max:
  cont=cont+1
  x= phi(x)
x_raiz=x
print(" ")
print("A solução encontrada foi",x_raiz)
print(" ")
print("teve", cont, "interações")