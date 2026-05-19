import math

def resolver_sistema_2x2(A, B):
    det_principal = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    if abs(det_principal) < 1e-15:
        raise ValueError("Sistema sem solução única.")
    det_x = B[0] * A[1][1] - A[0][1] * B[1]
    det_y = A[0][0] * B[1] - B[0] * A[1][0]
    return [det_x / det_principal, det_y / det_principal]

def algoritmo_thomas(a, b, c, d):
    n = len(b)
    c_prime = [0.0] * (n - 1)
    d_prime = [0.0] * n
    
    c_prime[0] = c[0] / b[0]
    d_prime[0] = d[0] / b[0]
    
    for i in range(1, n - 1):
        denominador = b[i] - a[i-1] * c_prime[i-1]
        c_prime[i] = c[i] / denominador
        d_prime[i] = (d[i] - a[i-1] * d_prime[i-1]) / denominador    
    d_prime[n-1] = (d[n-1] - a[n-2] * d_prime[n-2]) / (b[n-1] - a[n-2] * c_prime[n-2])
    x = [0.0] * n
    x[n-1] = d_prime[n-1]
    for i in range(n - 2, -1, -1):
        x[i] = d_prime[i] - c_prime[i] * x[i+1]
    return x

def calcular_coeficientes_spline(X, Y, tipo_fronteira="natural", valor_fronteira=0.0):
    n = len(X) - 1
    h = [X[i+1] - X[i] for i in range(n)]
    tamanho_sistema = n + 1
    sub_a = [0.0] * (tamanho_sistema - 1)
    diag_b = [0.0] * tamanho_sistema
    super_c = [0.0] * (tamanho_sistema - 1)
    termos_d = [0.0] * tamanho_sistema
    for i in range(1, n):
        sub_a[i-1] = h[i-1]
        diag_b[i] = 2 * (h[i-1] + h[i])
        super_c[i] = h[i]
        termos_d[i] = 6 * ((Y[i+1] - Y[i])/h[i] - (Y[i] - Y[i-1])/h[i-1])
    if tipo_fronteira == "natural":
        diag_b[0] = 1.0
        diag_b[n] = 1.0
        termos_d[0] = 0.0
        termos_d[n] = 0.0
    elif tipo_fronteira == "fixada_derivada2":
        diag_b[0] = 1.0
        diag_b[n] = 1.0
        termos_d[0] = valor_fronteira(X[0]) if callable(valor_fronteira) else valor_fronteira
        termos_d[n] = valor_fronteira(X[n]) if callable(valor_fronteira) else valor_fronteira
    M = algoritmo_thomas(sub_a, diag_b, super_c, termos_d)
    coeficientes = []
    for i in range(n):
        a_i = (M[i+1] - M[i]) / (6 * h[i])
        b_i = M[i] / 2
        c_i = (Y[i+1] - Y[i])/h[i] - (h[i]/6)*(M[i+1] + 2*M[i])
        d_i = Y[i]
        coeficientes.append((a_i, b_i, c_i, d_i))
    return coeficientes


def avaliar_spline(X, coeficientes, x_alvo):
    for i in range(len(X) - 1):
        if X[i] <= x_alvo <= X[i+1]:
            a, b, c, d = coeficientes[i]
            dx = x_alvo - X[i]
            return a * (dx**3) + b * (dx**2) + c * dx + d
    if x_alvo < X[0]:
        a, b, c, d = coeficientes[0]
        dx = x_alvo - X[0]
        return a * (dx**3) + b * (dx**2) + c * dx + d
    else:
        a, b, c, d = coeficientes[-1]
        dx = x_alvo - X[-2]
        return a * (dx**3) + b * (dx**2) + c * dx + d
    
def calcular_diferencias_divididas(X, Y):
    n = len(X)
    tabela = [[0.0] * n for _ in range(n)]
    for i in range(n):
        tabela[i][0] = Y[i]
    for j in range(1, n):
        for i in range(n - j):
            tabela[i][j] = (tabela[i+1][j-1] - tabela[i][j-1]) / (X[i+j] - X[i])
    return [tabela[0][i] for i in range(n)]

def avaliar_polinomio_newton(X, coefs, x_alvo):
    n = len(coefs)
    resultado = coefs[0]
    produto_acumulado = 1.0
    for i in range(1, n):
        produto_acumulado *= (x_alvo - X[i-1])
        resultado += coefs[i] * produto_acumulado
    return resultado


# ==============================================================================
# PROCESSAMENTO DOS PROBLEMAS
# ==============================================================================

print("=== EXERCÍCIO 1 ===")
X_ex1 = [1, 2, 3, 4, 5]
Y_bubble = [5, 21, 46, 81, 126]
Y_merge = [7, 18, 30, 43, 57]
sum_x4 = sum(x**4 for x in X_ex1)
sum_x2_yB = sum((X_ex1[i]**2) * Y_bubble[i] for i in range(len(X_ex1)))
alpha = sum_x2_yB / sum_x4
X_m = X_ex1[1:]
Y_m = Y_merge[1:]
sum_f_quadrado = sum((x * math.log2(x))**2 for x in X_m)
sum_f_yM = sum((X_m[i] * math.log2(X_m[i])) * Y_m[i] for i in range(len(X_m)))
beta = sum_f_yM / sum_f_quadrado
print(f"Tarefa 1: Equações obtidas:")
print(f"  Bubble Sort: g(x) = {alpha:.6f} * x^2")
print(f"  Merge Sort:  g(x) = {beta:.6f} * x * log2(x)")
instancia = 100
prev_bubble = alpha * (instancia**2)
prev_merge = beta * instancia * math.log2(instancia)
print(f"Tarefa 2: Projeção para x = 100:")
print(f"  Tempo Bubble Sort: {prev_bubble:.2f} ms")
print(f"  Tempo Merge Sort:  {prev_merge:.2f} ms\n")

print("=== EXERCÍCIO 2 ===")
T_ex2 = [0, 5, 10, 15, 20]
Theta_ex2 = [120, 95, 75, 60, 48]
Y_linearizado = [math.log(theta) for theta in Theta_ex2]
m = len(T_ex2)
sum_t = sum(T_ex2)
sum_t2 = sum(t**2 for t in T_ex2)
sum_Y = sum(Y_linearizado)
sum_tY = sum(T_ex2[i] * Y_linearizado[i] for i in range(m))
Matriz_A = [[m, sum_t], [sum_t, sum_t2]]
Vetor_B = [sum_Y, sum_tY]
A_0, A_1 = resolver_sistema_2x2(Matriz_A, Vetor_B)
theta_0 = math.exp(A_0)
k = -A_1
print("Tarefa 1: Modelo Exponencial Ajustado:")
print(f"  g(t) = {theta_0:.4f} * e^(-{k:.4f} * t)")
t_alvo = 17
theta_17 = theta_0 * math.exp(-k * t_alvo)
print(f"Tarefa 2: Temperatura estimada para t = 17 min: {theta_17:.2f} °C\n")

print("=== EXERCÍCIO 3 e 4: Splines da Tabela 1 ===")
X_tab1 = [0.50, 0.75, 1.00, 1.50, 2.00, 2.50, 3.00]
Y_tab1 = [-2.80, -0.60, 1.00, 3.20, 4.80, 6.00, 7.00]
coefs_nat_tab1 = calcular_coeficientes_spline(X_tab1, Y_tab1, tipo_fronteira="natural")
print("Exercício 3: Coeficientes das Splines Naturais gerados!")
print(f"  S_0(x) no primeiro intervalo: a={coefs_nat_tab1[0][0]:.4f}, b={coefs_nat_tab1[0][1]:.4f}, c={coefs_nat_tab1[0][2]:.4f}, d={coefs_nat_tab1[0][3]:.4f}")
funcao_fronteira = lambda x: math.exp(-x)
coefs_fixos_tab1 = calcular_coeficientes_spline(X_tab1, Y_tab1, tipo_fronteira="fixada_derivada2", valor_fronteira=funcao_fronteira)
print("\nExercício 4: Coeficientes com derivada S''=e^-x gerados!")
print(f"  S_0(x) modificado: a={coefs_fixos_tab1[0][0]:.4f}, b={coefs_fixos_tab1[0][1]:.4f}\n")

print("=== EXERCÍCIO 5 ===")
X_gas_dados = [1, 3, 4, 9]
Y_gas_dados = [20.0, 7.5, 6.5, 7.10]
coefs_gas = calcular_coeficientes_spline(X_gas_dados, Y_gas_dados, tipo_fronteira="natural")
consumo_mes_12 = avaliar_spline(X_gas_dados, coefs_gas, 12.0)
print(f"Consumo interpolado/extrapolado para o mês 12: {consumo_mes_12:.2f}\n")

print("=== QUESTÃO 4 ===")
X_q4 = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7]
Y_q4 = [math.sin(x) for x in X_q4]
coefs_q4 = calcular_coeficientes_spline(X_q4, Y_q4, tipo_fronteira="fixada_derivada2", valor_fronteira=math.pi)
alvos_q4 = [1.12, 1.35, 1.63]
print("Valores Interpolados de S_i(x):")
for alvo in alvos_q4:
    print(f"  S_i({alvo}) = {avaliar_spline(X_q4, coefs_q4, alvo):.6f}")
print()

print("=== QUESTÃO 5 ===")
X_q5 = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7]
Y_q5 = [math.cos(x) for x in X_q5]
coefs_newton = calcular_diferencias_divididas(X_q5, Y_q5)
print("Coeficientes Triangulares do Polinômio de Newton (d_i):")
for idx, c in enumerate(coefs_newton):
    print(f"  d_{idx} = {c:.6f}")