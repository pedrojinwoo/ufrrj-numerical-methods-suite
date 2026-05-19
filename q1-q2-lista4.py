import math

def systemSolver(A, B):
    detPrincipal = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    if abs(detPrincipal) < 1e-15:
        raise ValueError("Sistema sem solução única.")
    detX = B[0] * A[1][1] - A[0][1] * B[1]
    detY = A[0][0] * B[1] - B[0] * A[1][0]
    return [detX / detPrincipal, detY / detPrincipal]

print("=== EXERCÍCIO 1 ===")
Xex1 = [1, 2, 3, 4, 5]
Ybubble = [5, 21, 46, 81, 126]
Ymerge = [7, 18, 30, 43, 57]

sum_x4 = sum(x**4 for x in Xex1)
sum_x2_yB = sum((Xex1[i]**2) * Ybubble[i] for i in range(len(Xex1)))

alpha = sum_x2_yB / sum_x4
Xm = Xex1[1:]
Ym = Ymerge[1:]
sumFQuadrado = sum((x * math.log2(x))**2 for x in Xm)
sumFyM = sum((Xm[i] * math.log2(Xm[i])) * Ym[i] for i in range(len(Xm)))
beta = sumFyM / sumFQuadrado

print(f"Tarefa 1: Equações obtidas:")
print(f"  Bubble Sort: g(x) = {alpha:.6f} * x^2")
print(f"  Merge Sort:  g(x) = {beta:.6f} * x * log2(x)")
instancia = 100
prevBubble = alpha * (instancia**2)
prevMerge = beta * instancia * math.log2(instancia)
print(f"Tarefa 2: Projeção para x = 100:")
print(f"  Tempo Bubble Sort: {prevBubble:.2f} ms")
print(f"  Tempo Merge Sort:  {prevMerge:.2f} ms\n")



print("=== EXERCÍCIO 2 ===")
T_ex2 = [0, 5, 10, 15, 20]
Theta_ex2 = [120, 95, 75, 60, 48]
Y_linearizado = [math.log(theta) for theta in Theta_ex2]

m = len(T_ex2)
sumT = sum(T_ex2)
sumT2 = sum(t**2 for t in T_ex2)
sumY = sum(Y_linearizado)
sumTY = sum(T_ex2[i] * Y_linearizado[i] for i in range(m))
MatrizA = [[m, sumT], [sumT, sumT2]]
VetorB = [sumY, sumTY]
A0, A1 = systemSolver(MatrizA, VetorB)
theta_0 = math.exp(A0)
k = -A1  

print("Tarefa 1: Modelo Exponencial Ajustado:")
print(f"  g(t) = {theta_0:.4f} * e^(-{k:.4f} * t)")
t_alvo = 17
theta17 = theta_0 * math.exp(-k * t_alvo)
print(f"Tarefa 2: Temperatura estimada para t = 17 min: {theta17:.2f} °C\n")