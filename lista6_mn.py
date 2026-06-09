import matplotlib.pyplot as plt
#########################################
##      lista 6 - Métodos numéricos    ##
##      Aluno: Gustavo Simplicio,      ##
#               João França,           ##
#               Lohan Vieira,          ##
#               Pedro Costa e          ##
#               Miguel Nogueira        ##
##                                     ##
#########################################

h = 0.01
n = 15000 # t -> 150 dias / h
x0 = 1 
y0 = 1 
a = 0.2
b = 0.7
c = 0.4
d = 0.5


temposEuler = []
presasEuler = []
predadoresEuler = []
temposKH4 = []
presasKH4 = []
predadoresKH4 = []

## Implementação:
####### Método de Euler #########
def euler(fPresa, fPredador, x0, y0, h, n):
    
    t = 0
    x = x0
    y = y0

    for i in range(n):
        xnovo = x + h * fPresa(x, y) #dx
        ynovo = y + h * fPredador(x, y) #dy

        temposEuler.append(t)
        presasEuler.append(x)
        predadoresEuler.append(y)

        y = ynovo
        x = xnovo
        t += h # passagem do tempo
        

    return x, y


####### Método de Runge-Kutta 4a ##########
# ynovo -> calculado usando media ponderadas dos coeficientes de inclinação
# ynovo = y0 + h/6(k1 + 2k2 + 2 k3 + k)

# ki (coeficientes de inclinação)
    # k1 = fPresa(x, y)
    # k2 = fPresa(x + h/2 * k1,  y + h/2 * k1)
    # k3 = fPresa(x + h/2 * k2,  y + h/2 * k2)
    # k4 = fPresa(x + h * k3,  y + h * k3)


def RK4(fPresa, fPredador, x0, y0, h, n):
    t = 0
    x, y = x0, y0


    for i in range(n):

        kx1 = fPresa(x, y)
        ky1 = fPredador(x, y)

        kx2 = fPresa(x + h/2 * kx1,  y + h/2 * ky1)
        ky2 = fPredador(x + h/2 * kx1, y + h/2 * ky1)

        kx3 = fPresa(x + h/2 * kx2,  y + h/2 * ky2)
        ky3 = fPredador(x + h/2 * kx2, y + h/2 * ky2)

        kx4 = fPresa(x + h * kx3,  y + h * ky3)
        ky4 = fPredador(x + h * kx3, y + h * ky3)

        xnovo = x + h/6 * (kx1 + 2*kx2 + 2*kx3 + kx4)
        ynovo = y + h/6 * (ky1 + 2*ky2 + 2*ky3 + ky4)

        temposKH4.append(t)
        presasKH4.append(x)
        predadoresKH4.append(y)

        y = ynovo
        x = xnovo
        t += h # passagem do tempo
    
    return x, y


## Funções
funcPresa = lambda x, y: x *(a - b * y)
funcPredador = lambda x, y: y * (-c + d * x)

##
metodoEuler = euler(funcPresa, funcPredador, x0, y0, h, n)
metodoKH4 = RK4(funcPresa, funcPredador, x0, y0, h, n)

## Prints
print("\nInstante t = ", n * h)
print(f"Euler -> Presas: {presasEuler[n-1]:.6f}")
print(f"Euler -> Predadores: {predadoresEuler[n-1]:.6f}")

print(f"RK4   -> Presas: {presasKH4[n-1]:.6f}")
print(f"RK4   -> Predadores: {predadoresKH4[n-1]:.6f}")

print("Conclusao: \ntendo t = 150, os dois metodos se aproximam muito. Ao aumentar esse tempo(trocando n para um valor maior), \tpelo grafico, fica visivel que o metodo KH4 é mais estavel")
print("Isso se dá pois enquanto o euler calcula apenas uma curva de inclinacao a cada iteracao, enquanto o RK4 ultiliza 4 curvas de inclinacao e ainda ponderada.")


# Gráficos Matplot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Euler
ax1.plot(temposEuler, presasEuler, label='Presas')
ax1.plot(temposEuler, predadoresEuler, label='Predadores')
ax1.set_title('Método de Euler')
ax1.set_xlabel('Tempo')
ax1.set_ylabel('População')
ax1.legend()
ax1.grid(True)

# RK4
ax2.plot(temposKH4, presasKH4, label='Presas')
ax2.plot(temposKH4, predadoresKH4, label='Predadores')
ax2.set_title('Método de Runge-Kutta 4 Ordem')
ax2.set_xlabel('Tempo')
ax2.set_ylabel('População')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()

