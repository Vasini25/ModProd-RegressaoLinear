import math

#n = quantidade de pontos
#j = offset (valor x) do primeiro ponto
#proxpPontoX = valor noi eixo X ponto a ser calculado com a equação de reta encontrado (preferenciamente x+1)
#x[] = lista de pontos x
#y[] = lista de valores y nos pontos correspondentes
# a quantidade de valores na Lista y deve ser igual ao valor de n

#A partir de do valor 'FsOffset', considerar os 'FsBloco' primeiros valores num ciclo de 'FsCiclo' valores (default = 1, 1, 1)
def regressaoLinear(y, proxPontoX, FsBloco, FsCiclo, FsOffset):
    n = 0
    n = len(y)
    j = 1
    x = []

    #caso haja necessidade de calcular Fator de Sazonalidade
    FsBloco = 1
    FsCiclo = 4
    FsOffset = 1

    x = geraX(n, j)

    print("x = {}".format(x))
    print("y = {}".format(y))

    #calcula somatorios
    somX = sum(x)
    somY = sum(y)
    somXY = mpAndSum(x, y)
    somXquad = sumQuad(x)
    somYquad = sumQuad(y)

    print("\nSomatorios: \nx = {} \nx^2 = {} \ny = {} \ny^2 = {} \nx*y = {}".format(somX, somXquad, somY, somYquad, somXY))

    #calcula a e b da equação da reta (regressão linear)
    denominador = denominadorComum(n, somX, somXquad)
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
                offset += FsCiclo

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

#gera vetor (Lista) de pontos x
def geraX(n, j):
    x = []

    for i in range (n):
        x.append(i+j)

    return x

#retorna somatorio de um vetor
def sum(vector):
    n = len(vector)
    somatorio = 0

    for i in range(n):
        somatorio += vector[i]

    return somatorio

#retorna somatorio da multiplicação de dois elementos equivalentes de dois vetors
def mpAndSum(vector1, vector2):
    n = len(vector1)
    somatorio = 0

    for i in range(n):
        somatorio += (vector1[i] * vector2[i])

    return somatorio

#retorna somatorio dos valores ao quadrado de um vetor
def sumQuad(vector):
    n = len(vector)
    somatorio = 0

    for i in range(n):
        somatorio += (vector[i] ** 2)

    return somatorio

#retorna o denominador comum de a e b para seus respectivos calculos
def denominadorComum(n, somX, somXquad):
    denominador = ((n * somXquad) - (somX ** 2))

    return denominador
#calcula a e b da equação da reta (regressão linear)
#def calcA():
