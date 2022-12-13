#MÉTODO da secante
import math

def f(x):
  return math.exp(x) - 2 * x -1

#PRECISÃO DE 4 CASAS DECIMAIS
erro_max=0.0001

#  Valores para X
x_0=0.5
x_1 = 1.5
x=0.6
cont=0

while math.fabs(f(x))>erro_max:
  cont=cont+1
  x = (x_0*f(x_1)-x_1*f(x_0))/(f(x_1)-f(x_0))
  x_0=x_1
  x_1=x
        

print("A solução encontrada foi", x)
print(" ")
print("teve", cont, "interações")