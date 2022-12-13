import numpy as np


def VetorB(A): # NESSA FUNÇÃO SOMAMOS OS ELEMENTOS DA LINHA E ADICIONAMOS A SOMA EM UMA LISTA VAZIA
  lista = []
  for L in range(len(A)): # L = LINHAS E C = COLUNAS
      soma = 0
      for C in range(len(A[L])):
            soma += A[L][C]
      lista.append(soma)
  return lista


def elimGauss(A, b): #ESSA FUNÇÃO FAZ O ESCALONAMENTO NA MATRIZ TAL
  n = len(b) #DIMENSÃO DA MATRIZ
  for k in range(0, n-1):
      for L in range(k+1, n):
          m = A[L][k]/A[k][k]
          for C in range(k, n):
            A[L][C] = A[L][C]-m*A[k][C]
          b[L] = b[L]-m*b[k]
  return A, b


def subsReversa(A, b): # Aqui nessa função é executado a substituição reversa, já que não devemos usar o pivotamento
   n = len(b)
   x = n*[0]
   x[n-1] = b[n-1]/A[n-1][n-1]
   for k in range(n-2, -1, -1):
     s = 0
     for C in range(k+1, n):
       s = s + A[k][C]*x[C]
     x[k] = (b[k]-s)/A[k][k]
   return x


def matrizHil(a, z): # Essa função constroi uma matriz de hilbert com os parametros que o usuário passar, por exemplo 3p3
    if a == z:
      return [[1 / (L + C + 1) for C in range(z)] for L in range(a)]
    else:
      print("Essa forma de matriz não é valida")



# main
a = int(input("insira o número de linhas da sua matriz: "))
z = int(input("insira o número de colunas da sua matriz: "))
resp = print("Sua matriz é do tamanho ",a ,"x",z)
A = matrizHil(a, z)
b = VetorB(A)

print("-------------------------- GAUSS ---------------------------------------")
print("Sua matriz após o método de eliminação de gauss é :", elimGauss(A, b))
print("------------------------- SUBSREVERSA ----------------------------------")
print("Sua matriz após o método da substituição reversa é :",subsReversa(A, b))
print("------------------------------------------------------------------------")