#heuristica que conta quantos numeros estão fora do lugar
def h1(matriz_init, matriz_obj):
    contador = 0
    for i in range(3):
        for j in range(3):
            if (matriz_init[i][j] != matriz_obj[i][j]):
                if(matriz_init[i][j] != 0):
                    contador += 1

    return contador

# Distãncia de Manhattan - Heurística 2
def h2(matriz_init, matriz_obj):
    dist = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    if (matriz_obj[i][j] == matriz_init[k][l]):
                        if(matriz_init[k][l] != 0 and matriz_obj[i][j] != 0):
                            dist += abs(i-k) + abs(j-l)

    return dist
