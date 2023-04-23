import regressao_linear as rl

if __name__ == '__main__':
    y = [11, 20, 51, 22, 13, 31, 60, 28, 12, 39, 62, 40, 23, 25, 88, 45]

    #valores para calculo do Fator de Sazonalidade
    FsBloco = 1
    FsCiclo = 4
    FsOffset = 1

    rl.regressaoLinear(y, 17, 1, FsBloco, FsCiclo, FsOffset)