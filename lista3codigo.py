import numpy as np

def resolver_mmq_detalhado(x, y, label="Questão"):
  n = len(x)
  sum_x = np.sum(x)
  sum_y = np.sum(y)
  sum_x2 = np.sum(x**2)
  sum_xy = np.sum(x * y)
  
  print(f"\n--- JUSTIFICATIVA: TABELA DE SOMATÓRIOS ({label}) ---")
  print(f"{'i':<4} | {'x':<10} | {'y':<10} | {'x^2':<10} | {'x*y':<10}")
  print("-" * 55)
  for i in range(n):
    print(f"{i:<4} | {x[i]:>10.4f} | {y[i]:>10.4f} | {x[i]**2:>10.4f} | {x[i]*y[i]:>10.4f}")
  
  print("-" * 55)
  print(f"SUM  | {sum_x:>10.4f} | {sum_y:>10.4f} | {sum_x2:>10.4f} | {sum_xy:>10.4f}")
  
  # Sistema: 
  # (sum_x2)a + (sum_x)b = sum_xy
  # (sum_x)a  + (n)b     = sum_y
  A = np.array([[sum_x2, sum_x], [sum_x, n]])
  B = np.array([sum_xy, sum_y])
  a, b = np.linalg.solve(A, B)
  
  print(f"\nEquações Normais Resultantes:")
  print(f"{sum_x2:.4f}a + {sum_x:.4f}b = {sum_xy:.4f}")
  print(f"{sum_x:.4f}a + {n}b = {sum_y:.4f}")
  print(f"Resultado: a = {a:.6f}, b = {b:.6f}")
  return a, b

# Dados Questão 1
t1 = np.array([0.5, 0.75, 1.0, 1.5, 2.0, 2.5, 3.0])
y1 = np.array([-2.8, -0.6, 1.0, 3.2, 4.8, 6.0, 7.0])
resolver_mmq_detalhado(t1, y1, "Questão 1")


def imprimir_ajuste(nome, coefs, formula):
    print(f"\n--- Item {nome} ---")
    print(f"Fórmula: {formula}")
    print(f"Coeficientes encontrados: {coefs}")

# Dados da Tabela 2
x = np.array([-8, -5.71428571, -3.42857143, -1.14285714, 1.14285714, 3.42857143, 5.71428571, 8])
y = np.array([1.06635918, 0.80014487, 0.64216079, 0.54170856, 0.44962931, 0.39317197, 0.33772819, 0.31377657])

# a) g(x) = ax + b
# polyfit retorna [a, b] para grau 1
res_a = np.polyfit(x, y, 1)
imprimir_ajuste("a) Linear", res_a, "g(x) = ax + b")

# b) g(x) = ax^2 + bx + c
# polyfit retorna [a, b, c] para grau 2
res_b = np.polyfit(x, y, 2)
imprimir_ajuste("b) Quadrática", res_b, "g(x) = ax^2 + bx + c")

# c) g(x) = ax^3 + bx^2 + cx
# Aqui o coeficiente 'd' (constante) é zero por definição da questão
# Usamos matriz de Vandermonde customizada
A_c = np.vstack([x**3, x**2, x]).T
res_c, _, _, _ = np.linalg.lstsq(A_c, y, rcond=None)
imprimir_ajuste("c) Cúbica (sem constante)", res_c, "g(x) = ax^3 + bx^2 + cx")

# d) g(x) = 1 / (ax + b)
# Linearização: Y = 1/y -> Y = ax + b
Y_linear = 1/y
res_d = np.polyfit(x, Y_linear, 1)
imprimir_ajuste("d) Hiperbólica (Linearizada)", res_d, "g(x) = 1 / (ax + b)")

# e) Comparação (Cálculo do R^2 simplificado)
def calcular_r2(x, y, modelo_func):
  y_pred = modelo_func(x)
  residuos = y - y_pred
  ss_res = np.sum(residuos**2)
  ss_tot = np.sum((y - np.mean(y))**2)
  return 1 - (ss_res / ss_tot)

print("\n--- Item e) Comparação de Qualidade (R²) ---")
r2_a = calcular_r2(x, y, lambda x: res_a[0]*x + res_a[1])
r2_b = calcular_r2(x, y, lambda x: res_b[0]*x**2 + res_b[1]*x + res_b[2])
r2_c = calcular_r2(x, y, lambda x: res_c[0]*x**3 + res_c[1]*x**2 + res_c[2]*x)
r2_d = calcular_r2(x, y, lambda x: 1/(res_d[0]*x + res_d[1]))

modelos = {'A': r2_a, 'B': r2_b, 'C': r2_c, 'D': r2_d}
melhor_modelo = max(modelos, key=modelos.get)

print(f"R² Modelo A (Linear): {r2_a:.6f}")
print(f"R² Modelo B (Quadrático): {r2_b:.6f}")
print(f"R² Modelo C (Cúbico): {r2_c:.6f}")
print(f"R² Modelo D (Hiperbólico): {r2_d:.6f}")
print(f"Melhor Modelo: {melhor_modelo} (R² = {modelos[melhor_modelo]:.6f})")
