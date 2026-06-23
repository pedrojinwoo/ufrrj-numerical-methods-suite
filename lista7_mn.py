# Aluno: Pedro Costa da Motta
# Matrícula: 20240014240


import numpy as np
import matplotlib.pyplot as plt

# ============================================
# MÉTODOS DE PASSO ÚNICO PARA SOLUÇÃO DE PVI
# ============================================
def euler_passo(f, x, y, h):
    return y + h * f(x, y)
def rk2_passo(f, x, y, h):
    k1 = f(x, y)
    k2 = f(x + h, y + h * k1)
    return y + (h / 2) * (k1 + k2)
def rk3_passo(f, x, y, h):
    k1 = f(x, y)
    k2 = f(x + h / 2, y + (h / 2) * k1)
    k3 = f(x + h, y - h * k1 + 2 * h * k2)
    return y + (h / 6) * (k1 + 4 * k2 + k3)
def rk4_passo(f, x, y, h):
    k1 = f(x, y)
    k2 = f(x + h / 2, y + (h / 2) * k1)
    k3 = f(x + h / 2, y + (h / 2) * k2)
    k4 = f(x + h, y + h * k3)
    return y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
METODOS = {"Euler": euler_passo, "RK2": rk2_passo, "RK3": rk3_passo, "RK4": rk4_passo}
def resolver_pvi(f, x0, y0, h, x_final, metodo):
    n_passos = round((x_final - x0) / h)
    xs = np.zeros(n_passos + 1)
    ys = np.zeros(n_passos + 1)
    xs[0], ys[0] = x0, y0
    passo_funcao = METODOS[metodo]
    for i in range(n_passos):
        ys[i + 1] = passo_funcao(f, xs[i], ys[i], h)
        xs[i + 1] = x0 + (i + 1) * h
    return xs, ys

# ================================
# QUESTÃO 1 e GERAÇÃO DO GRÁFICO
# ================================
print()
print()
print("QUESTÃO 1")
f1 = lambda x, y: -y + x + 2
exata1 = lambda x: np.exp(-x) + x + 1
x0_1, y0_1, h_1, xf_1 = 0.0, 2.0, 0.1, 1.0
resultados1 = {}
for m in ["RK2", "RK3", "RK4"]:
    xs1, ys1 = resolver_pvi(f1, x0_1, y0_1, h_1, xf_1, m)
    resultados1[m] = ys1
xs_grade = xs1
ys_exata1 = exata1(xs_grade)
print(f"{'x':>6} | {'RK2':>10} | {'RK3':>10} | {'RK4':>10} | {'Exata':>10}")
for i in range(len(xs_grade)):
    print(f"{xs_grade[i]:6.2f} | {resultados1['RK2'][i]:10.6f} | {resultados1['RK3'][i]:10.6f} | "
          f"{resultados1['RK4'][i]:10.6f} | {ys_exata1[i]:10.6f}")
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), dpi=100, height_ratios=[2, 1.2])
ax1.plot(xs_grade, ys_exata1, '-', color='#111111', linewidth=2, label='Solução Exata')
ax1.plot(xs_grade, resultados1['RK2'], 'o--', color='#4C72B0', label='RK 2ª Ordem')
ax1.plot(xs_grade, resultados1['RK3'], 's--', color='#DD8452', label='RK 3ª Ordem')
ax1.plot(xs_grade, resultados1['RK4'], '^--', color='#55A868', label='RK 4ª Ordem')
ax1.set_title("Comparativo de Métodos de Runge-Kutta (Questão 1)")
ax1.set_xlabel("x")
ax1.set_ylabel("y(x)")
ax1.legend()
ax1.grid(True, alpha=0.3)
ax2.semilogy(xs_grade, np.abs(resultados1['RK2'] - ys_exata1) + 1e-16, 'o--', color='#4C72B0', label='Erro RK2')
ax2.semilogy(xs_grade, np.abs(resultados1['RK3'] - ys_exata1) + 1e-16, 's--', color='#DD8452', label='Erro RK3')
ax2.semilogy(xs_grade, np.abs(resultados1['RK4'] - ys_exata1) + 1e-16, '^--', color='#55A868', label='Erro RK4')
ax2.set_xlabel("x")
ax2.set_ylabel("Erro Absoluto (Log)")
ax2.legend()
ax2.grid(True, alpha=0.3, which='both')

plt.tight_layout()
plt.show()

# ============
# QUESTÃO 2
# ============
print()
print()
print("QUESTÃO 2 (Extrapolação até x = 1.5)")
xf_2 = 1.5
_, ys2_euler = resolver_pvi(f1, x0_1, y0_1, h_1, xf_2, "Euler")
_, ys2_rk4 = resolver_pvi(f1, x0_1, y0_1, h_1, xf_2, "RK4")
y_real_15 = exata1(xf_2)
print(f"Euler: y(1.5) = {ys2_euler[-1]:.6f} | Erro = {abs(ys2_euler[-1] - y_real_15):.2e}")
print(f"RK4:   y(1.5) = {ys2_rk4[-1]:.6f} | Erro = {abs(ys2_rk4[-1] - y_real_15):.2e}")
print(f"Exata: y(1.5) = {y_real_15:.6f}")

# ============
# QUESTÃO 3
# ============
print()
print()
print("QUESTÃO 3 (Cálculo em x = 1.25)")
f3 = lambda x, y: (x**2 * y - 2) / x
x0_3, y0_3, h_3, xf_3 = 1.0, 3.0, 0.01, 1.25
_, ys3_euler = resolver_pvi(f3, x0_3, y0_3, h_3, xf_3, "Euler")
_, ys3_rk4 = resolver_pvi(f3, x0_3, y0_3, h_3, xf_3, "RK4")
print(f"Euler: y(1.25) = {ys3_euler[-1]:.6f}")
print(f"RK4:   y(1.25) = {ys3_rk4[-1]:.6f}")
print(f"Diferença absoluta entre os métodos: {abs(ys3_euler[-1] - ys3_rk4[-1]):.6f}")

# ============
# QUESTÃO 4
# ============
print()
print()
print("QUESTÃO 4 (Integração sem Scipy - h = 10^-5)")
f4_pura = lambda x: 6 * x**2 - 1 / x**2 + 3
exata4 = lambda x: 2 * x**3 + 1 / x + 3 * x - 2030.1
x0_4, y0_4, h_4, xf_4 = 10.0, 0.0, 1e-5, 16.0
n_passos4 = round((xf_4 - x0_4) / h_4)
xs4 = np.linspace(x0_4, xf_4, n_passos4 + 1)
y_derivadas = f4_pura(xs4)
y16_euler = y0_4 + h_4 * np.sum(y_derivadas[:-1])
y16_rk2 = y0_4 + h_4 * (np.sum(y_derivadas) - 0.5 * (y_derivadas[0] + y_derivadas[-1]))
y16_exata = exata4(xf_4)
print(f"Euler: y(16) = {y16_euler:.6f} | Erro = {abs(y16_euler - y16_exata):.2e}")
print(f"RK2:   y(16) = {y16_rk2:.6f} | Erro = {abs(y16_rk2 - y16_exata):.2e}")
print(f"Exata: y(16) = {y16_exata:.6f}")

# ============
# QUESTÃO 5
# ============
print()
print()
print("QUESTÃO 5 (Erro Máximo no Intervalo)")
f5 = lambda x, y: -2 * x * y**2
exata5 = lambda x: 1 / (x**2 + 2)
x0_5, y0_5, h_5, xf_5 = 0.0, 0.5, 0.001, 1.0
xs5, ys5_euler = resolver_pvi(f5, x0_5, y0_5, h_5, xf_5, "Euler")
_, ys5_rk3 = resolver_pvi(f5, x0_5, y0_5, h_5, xf_5, "RK3")
ys5_exata = exata5(xs5)
erros_euler5 = np.abs(ys5_euler - ys5_exata)
erros_rk3_5 = np.abs(ys5_rk3 - ys5_exata)
idx_max_e = np.argmax(erros_euler5)
idx_max_r3 = np.argmax(erros_rk3_5)
print(f"Erro Máximo Euler: {erros_euler5[idx_max_e]:.6e} obtido em x = {xs5[idx_max_e]:.3f}")
print(f"Erro Máximo RK3:   {erros_rk3_5[idx_max_r3]:.6e} obtido em x = {xs5[idx_max_r3]:.3f}")

# ============
# QUESTÃO 6
# ============
print()
print()
print("QUESTÃO 6 (Tabela de Erros Locais)")
f6 = lambda x, y: x * np.sqrt(x**2 + 5)
exata6 = lambda x: (1 / 3) * (np.sqrt(x**2 + 5))**3 - 1
x0_6, y0_6, h_6, xf_6 = 2.0, 8.0, 0.1, 3.0
xs6, ys6_euler = resolver_pvi(f6, x0_6, y0_6, h_6, xf_6, "Euler")
_, ys6_rk2 = resolver_pvi(f6, x0_6, y0_6, h_6, xf_6, "RK2")
ys6_exata = exata6(xs6)
erros_euler6 = np.abs(ys6_euler - ys6_exata)
erros_rk2_6 = np.abs(ys6_rk2 - ys6_exata)
print(f"{'x':>5} | {'Euler':>10} | {'RK2':>10} | {'Exata':>10} | {'Erro Euler':>12} | {'Erro RK2':>10}")
for i in range(len(xs6)):
    print(f"{xs6[i]:5.1f} | {ys6_euler[i]:10.6f} | {ys6_rk2[i]:10.6f} | {ys6_exata[i]:10.6f} | "
          f"{erros_euler6[i]:12.6e} | {erros_rk2_6[i]:10.6e}")
print(f"\nErro máximo global do método de Euler: {np.max(erros_euler6):.6e}")
print(f"Erro máximo global do método de RK2:   {np.max(erros_rk2_6):.6e}")