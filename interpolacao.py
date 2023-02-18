def p(x, a): #método de Horner para resolver polinômio
  r = 0
  n = len(a) #grau do polinõmio
  for i in range(0, n):
    r += a[i] * (x**i)
    return r

def elimGauss(A, b): #ESSA FUNÇÃO FAZ O ESCALONAMENTO NA MATRIZ TAL
    n = len(b) #DIMENSÃO DA MATRIZ
    for k in range(0, n-1):
        for L in range(k+1, n):
          m = A[L][k]/A[k][k]
          for C in range(k, n):
            A[L][C] = A[L][C]-m*A[k][C]
          b[L] = b[L]-m*b[k]
        return A, b

def solucao(A, b):
     #A função solucao(A, b) resolve um sistema linear triangular superior Ax = b. 
     #A função recebe como entrada a matriz triangular superior A e o vetor modificado b, e retorna a solução x
   n = len(b)
   x = n*[0]
   x[n-1] = b[n-1]/A[n-1][n-1]
   for k in range(n-2, -1, -1):
     s = 0
     for j in range(k+1, n):
       s = s + A[k][j]*x[j]
     x[k] = (b[k]-s)/A[k][k]
   return x


def MatrizVandermonde(x):
     #A função MatrizVandermonde(x) recebe um vetor x de valores e retorna a matriz de Vandermonde associada a esse vetor. 
     #A matriz de Vandermonde é uma matriz quadrada cujas entradas são potências crescentes dos elementos do vetor.
    n = len(x)
    V = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(x[i]**j)
        V.append(row)
    return V
  

x = [30, 35,40 ]  #graus da minha tabela, onde se encontra a temperatura 32,5°
fx = [0.99826, 0.99818,0.99828] #valores dos respectivos calor específicos

w = [20, 25, 30, 35, 40, 45, 50] #todos os meus graus
z = [0.99907, 0.99852, 0.99826, 0.99818, 0.99828, 0.99849, 0.99878] #seus respectivos calor específicos 

M1 = MatrizVandermonde(x)
#as matrizes de Vandermonde associadas aos vetores x e w. 
M2 = MatrizVandermonde(w)

M1_vt, x_t = elimGauss(M1, fx)
S1 = solucao(M1_vt, x_t)
#a função Gauss e solucao são usadas para obter os coeficientes dos polinômios que aproximam as curvas em questão. 
M2_t, y_t = elimGauss(M2, z)
S2 = solucao(M2_t, y_t)

print("com um polinômio de grau 2 temos:", p(32.5, S1)) #cálculo de um ponto específico
print("com um polinômio de grau 6 trmos:", p(32.5, S2))