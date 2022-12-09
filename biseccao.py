#MÉTODO DA BISSECÇÃO
import math

def f(x):
  return math.exp(x) - 2 * x -1

#INTERVALOS (B TEM QUE SER MAIOR QUE A)
  
a= 1
b= 2
cont=0

#PRECISÃO DE 4 CASAS DECIMAIS
erro_max=0.0001

#CÁLCULO PARA A M (MÉDIA)

while b-a > erro_max:
  print("A =",a,"B =",b)
  MD=(a+b)/2
  if f(a)*f(MD)<0:
    b=MD
  else: 
    a=MD
  
  cont=cont+1
  
print(" ")
print("A solução encontrada foi",MD)
print(" ")
print("teve", cont, "interações")