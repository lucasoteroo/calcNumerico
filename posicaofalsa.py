#MÉTODO DA Posição falsa
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
MD=(a+b)/2
if f(a)*f(b)<0:
  while math.fabs(f(MD))>erro_max:
    MD=(a*f(b)-b*f(a))/(f(b)-f(a))
    cont=cont+1
    if f(a)*f(MD)<0:
      b=MD
    else:
      a=MD
   

 
   
print(" ")
print("A solução encontrada foi",MD)
print(" ")
print("teve", cont, "interações")