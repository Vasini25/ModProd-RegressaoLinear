# Press Shift+F10 to execute it or replace it with your code.
import math

#n = quantidade de pontos
#j = offset (valor x) do primeiro ponto
#proxpPontoX = valor noi eixo X ponto a ser calculado com a equação de reta encontrado (preferenciamente x+1)
#x[] = lista de pontos x
#y[] = lista de valores y nos pontos correspondentes
# a quantidade de valores na Lista y deve ser igual ao valor de n

#A partir de do valor 'FsOffset', considerar os 'FsBloco' primeiros valores num ciclo de 'FsCiclo' valores (default = 1, 1, 1)
def calc():
    n = 16
    j = 1
    proxPontoX = n+1
    x = []
    y = [11, 20, 51, 22, 13, 31, 60, 28, 12, 39, 62, 40, 23, 25, 88, 45]

    #caso haja necessidade de calcular Fator de Sazonalidade
    FsBloco = 1
    FsCiclo = 4
    FsOffset = 1

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
    proxPontoY = (b*proxPontoX) + a
    print("Portanto, para o proximo ponto (x = {}), estima-se:\n y = {}\n".format(proxPontoX, proxPontoY))

    #calcula fator de correlação
    denominador = math.sqrt(denominador * ((n * somYquad) - (somY **2)))
    r = (nominadorB) / (denominador)
    print("Fator de correlação r = {}".format(r))

    if(r>0.7):
        print("Bom fator de correlação!\n\n\n")
    else:
        print("Mau fator de correlação!\n\n\n")
        P = []
        Ft = []
        somFt = 0
        contador = 0
        offset = FsOffset - 1

        for i in range(n):
            P.append(a + (b*x[i]))
            Ft.append(y[i]/P[i])

            if((contador < FsBloco) and (i >= offset)):
                somFt += Ft[i]
                contador += 1

            if ((i+1) % FsCiclo == 0):
                contador = 0
                offset += FsBloco

        print("Portanto, calculando o fator de sazonalidade:")
        print("P = {}".format(P))
        print("Ft = {}\n".format(Ft))
        ciclos = n/FsCiclo
        Fs = somFt/(ciclos * FsBloco)
        print("Fs = {}\n".format(Fs))

        DadoCorrigidoComFs = proxPontoY * Fs
        print("Valor no ponto x = {} corrigido pelo Fator de Sazonalidade:".format(proxPontoX))
        print(DadoCorrigidoComFs)
        print("\n\n\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calc()