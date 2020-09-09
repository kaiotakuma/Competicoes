def soma_diagonal_principal(m, t):
    soma = 0
    for i in range(t):
        for j in range(t):
            if (i == j):
                soma = soma + m[i][j]
    return soma


def analisa_linha(m):
    for i in m:
        if (m.count(i) > 1):
            return 1  # repetio elementos na linha
    return 0  # Linha sem elementos repetidos


def analise_linha_mat(m):
    cont = 0
    for i in m:
        if (analisa_linha(i) == 1):
            cont = cont + 1
    return cont


def analisaColuna(m, t):
    aux = list()
    cont = 0
    for i in range(t):
        for n in (m):
            aux.append(n[i])
        if (analisa_linha(aux) == 1):
            cont = cont + 1
        aux.clear()
    return cont


def ler(t):
    m = []
    for i in range(t):
        m.append(list(map(int, input().split())))
    return m


n = int(input())  # Numero de casos
for i in range(1,n+1):
    t = int(input())  # Tamanho da matriz
    mat = ler(t)
    print("Case #{}: {} {} {}".format(i, soma_diagonal_principal(mat, t), analise_linha_mat(mat), analisaColuna(mat, t)))
