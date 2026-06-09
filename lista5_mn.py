# Lista 5 - Métodos Numéricos
# Aluno: Pedro Costa da Motta
# Matrícula: 20240014240

import math

def metodo_trapezio_composto(funcao, a, b, n):
    h = (b - a) / n
    x = []
    for i in range(n + 1):
        x.append(a + i*h)
    sum = 0
    for i in range(1, n):
        sum += funcao(x[i])
    return h/2 * (funcao(x[0]) + 2*sum + funcao(x[n]))    
def metodo_trapezio_tabela(x, y):
    n = len(y) - 1
    h = x[1] - x[0]
    return (h/2)*(y[0] + 2*sum(y[1:-1]) + y[-1])
def metodo_simpson_13(funcao, a, b, n):
    if n % 2 != 0:
        raise ValueError("Para o metodo de Simpson 1/3, 'n' deve ser um número PAR.")
    h = (b - a) / n
    x = []
    for i in range(n + 1):
        x.append(a + i*h)
    soma_impar = 0
    soma_par = 0
    for i in range(1, n):
        if i % 2 != 0:
            soma_impar += funcao(x[i])
        else:
            soma_par += funcao(x[i])
    return h/3 * (funcao(x[0]) + 4*soma_impar + 2*soma_par + funcao(x[n]))
def metodo_s13_tabela(x, y):
    n = len(y) - 1
    h = (x[1] - x[0]) 
    if n % 2 != 0:
        raise ValueError("Para o metodo de Simpson 1/3, 'n' deve ser um número PAR.")
    soma_impar = 0
    soma_par = 0
    for i in range(1, n):
        if i % 2 != 0:
            soma_impar += y[i]
        else:
            soma_par += y[i]
    return (h/3) * (y[0] + 4*soma_impar + 2*soma_par + y[n])
def metodo_simpson_38(funcao, a, b, n):
    if n % 3 != 0:
        raise ValueError("Para o metodo de Simpson 3/8 'n' deve ser MuLTIPLO DE 3.")
    h = (b - a) / n
    x = []
    for i in range(n + 1):
        x.append(a + i*h)
    soma_nao_mult_3 = 0
    soma_mult_3 = 0
    for i in range(1, n):
        if i % 3 == 0:
            soma_mult_3 += funcao(x[i])
        else:
            soma_nao_mult_3 += funcao(x[i])
    return 3*h/8 * (funcao(x[0]) + 3*soma_nao_mult_3 + 2*soma_mult_3 + funcao(x[n]))
def metodo_s38_tabela(x, y):
    n = len(y) - 1
    h = x[1] - x[0]
    if n % 3 != 0:
        raise ValueError("n não é multiplo de 3")
    soma_mult3 = 0
    soma_nMult3 = 0
    for i in range(1, n):
        if(i % 3 == 0): 
            soma_mult3 += y[i]
        else:  
            soma_nMult3 += y[i]
    return (3 * h/8) * (y[0] + 3 * soma_nMult3 + 2 * soma_mult3 + y[n])

## PRIMEIRA QUESTÃO
func1 = lambda x: math.exp(x/2)/x
print("######### 1 - Primeira questao #########")
print("\nResultados obtidos:")
I_trap = metodo_trapezio_composto(func1, 1, 4, 30)
print(f"Trapezio Composto: {I_trap}")
I_s13 = metodo_simpson_13(func1, 1, 4, 30)
print(f"Simpson 1/3:       {I_s13}")
I_s38 = metodo_simpson_38(func1, 1, 4, 30)
print(f"Simpson 3/8:       {I_s38}")

## SEGUNDA QUESTÃO
func2 = lambda x: 1/ (1 + x)
print("\n######### 2 - Segunda questao #########")
print("\nResultados obtidos:")
I_trap = metodo_trapezio_composto(func2, 2, 4, 300)
print(f"Trapezio Composto: {I_trap}")
I_s13 = metodo_simpson_13(func2, 2, 4, 300)
print(f"Simpson 1/3:       {I_s13}")
I_s38 = metodo_simpson_38(func2, 2, 4, 300)
print(f"Simpson 3/8:       {I_s38}\n")


## QUESTÃO 3
print("###### 3 - Terceira questao ######")
func3 = lambda x: x **2
I_correto = 1/3
i = 1
tolerancia = 0.00005
while True:
    I = metodo_trapezio_composto(func3, 0, 1, i)
    erro = abs(I_correto - I)
    if(erro < tolerancia):
        break
    i += 1
print("Numero de subintervalos :", i)

## QUESTãO 4
print("\n###### 4 - Quarta questao ######")
x = [0,2,4,6,8,10]
y = [15, 80, 120, 150, 90, 25]
h = 10 - 0
I = metodo_trapezio_tabela(x, y)
print(f"Estimativa total MB/s transferido no intervalo foi: {I} MB/s\n")

# QUESTÃO 5
print("###### 5 - Quinta questao ######")
x = [0.0, 0.5, 1.0, 1.5, 2.0]
y = [10.0, 45.5, 85.2, 60.1, 15.0]
dados = dict(zip(x, y))
func5 = lambda x: dados[x]
I = metodo_simpson_13(func5, 0, 2, 4)
print(f"Estimativa total de energia consumida no intervalo foi: {round(I,2)} mJ")

# QUESTÃO 6
print("\n###### 6 - Sexta questao ######")
x = [0.00, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90]
y = [0.00, 3.39, 3.51, 3.32, 3.08, 2.82, 2.51, 2.26, 2.02, 1.78]
I = metodo_s38_tabela(x, y)
print(f"Estimativa total de dados liberados no intervalo foi: {round(I, 2)} GB")

# QUESTÃO 7
print("\n###### 7 - Setima questao ######")
im = [0.106, 0.806, 0.487, 1.054, 1.022, 1.438, 1.366, 0.995, 2.008, 1.132, 1.129, 1.713, 1.494]
m =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
h = m[1] - m[0] # b - a
I_trap  = metodo_trapezio_tabela(m, im)
I_s13   = metodo_s13_tabela(m, im)
I_s38   =  metodo_s38_tabela(m, im)
print("Estimativa total aproximada de instruçoes executadas\n\nRESULTADOS:")
print("Trapezio:\t", round(I_trap,3))
print("Simp. 1/3:\t", round(I_s13,3))
print("Simp. 3/8:\t", round(I_s38,3))

# QUESTÃO 8
print("\n###### 8 - Oitava questao ######")
x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 12, 35, 40, 28, 10, 2]
dados = dict(zip(x, y))
func8 = lambda x: dados[x]
I = metodo_trapezio_tabela(x, y)
print(f"Estimativa do acumulo de pacotes no intervalo foi: {round(I, 2)} pacotes\n")

# QUESTÃO 9
print("###### 9 - Nona questao ######")
x = [0, 1, 2, 3, 4, 5, 6]
y = [6.384, 15.595, 15.001, 22.846, 18.266, 9.586, 7.799]
dados = dict(zip(x,y))
func9 = lambda x: dados[x]
I = metodo_s13_tabela(x,y)
print(f"Estimativa total de corrente drenado:{round(I, 2)} mA")