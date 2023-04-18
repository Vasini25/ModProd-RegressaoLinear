# Press Shift+F10 to execute it or replace it with your code.
import math

#n = quantidade de pontos
#j = offset (valor x) do primeiro ponto
#x[] = lista de pontos x
#y[] = lista de valores y nos pontos correspondentes
# a quantidade de valores na Lista y deve ser igual ao valor de n
def calc():
    n = 10
    j = 1
    x = []
    y = [15, 18, 12, 12, 20, 14, 18, 17, 14, 20]

    for i in range (n):
        x.append(i+j)

    print("x = {}".format(x))
    print("y = {}".format(y))

    #calcula somatorios
    somX = 0
    somXquad = 0
    somY = 0
    somYquad = 0
    somXY = 0

    for i in range (n):
        somX += x[i]
        somXquad += x[i] **2
        somY += y[i]
        somYquad += y[i] **2
        somXY += x[i] * y[i]

    print("\nSomatorios: \nx = {} \nx^2 = {} \ny = {} \ny^2 = {} \nx*y = {}".format(somX, somXquad, somY, somYquad, somXY))

    #calcula a e b da equação da reta (regressão linear)
    denominador = ((n * somXquad) - (somX ** 2))
    a = ((somXquad * somY) - (somX * somXY)) / denominador
    nominadorB = (n * somXY) - (somX * somY)
    b = nominadorB / denominador

    print("\na = {} \nb = {}\n".format(a, b))
    print("Equação da reta:\nY = {} + {}x\n".format(a, b))

    #calcula valor do proximo ponto
    proxPontoX = x[n - 1] + 1
    proxPontoY = (b*proxPontoX) + a
    print("Portanto, para o proximo ponto (x = {}), estima-se:\n y = {}\n".format(proxPontoX, proxPontoY))

    #calcula fator de correlação
    denominador = math.sqrt((denominador) * ((n * somYquad) - (somY **2)))
    r = (nominadorB) / (denominador)
    print("Fator de correlação r = {}".format(r))

    if(r>0.7):
        print("Bom fator de correlação!\n\n\n")
    else:
        print("Mau fator de correlação!\n\n\n")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calc()