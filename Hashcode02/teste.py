def printafecha(n,lista):
    for i in range(int(n)):
        lista.append(')')
def printaAbre(n,lista):
    for i in range(int(n)):
        lista.append('(')

def diferenca(n,lista):
    #n = atual - ant
    # Positivo ( , Negativo )
    if(n>0):
        for i in range(n):
            lista.append('(')
    else:
        n = n * (-1)
        for i in range(n):
            lista.append(')')


def adicionaParenteses(l):
    lista = []
    for i in range(len(l)):
        if l[i] == '0' and i != 0:
            #ult_valor = lista[len(lista) - 1]
            #printafecha(ult_valor,lista)
            if(l[i-1] != '0'):
                lista.append('0')
            else:
                lista.append('0')

        elif(l[i] == '0'):
            lista.append('0')

        else:
            if(i ==0 and l[i] != '0'):
                n = l[i]
                printaAbre(n, lista)
                lista.append(l[i])
                if ((i < len(l) - 1) and l[i + 1] == '0' ):
                    n = l[i]
                    printafecha(n, lista)
            elif((i > 0) and (l[i - 1] == l[i])):
                lista.append(l[i])
                if ((i < len(l) - 1) and l[i + 1] == '0' ):
                    n = l[i]
                    printafecha(n, lista)
            else:
                n = int(l[i]) - int(l[i - 1])
                diferenca(n, lista)
                lista.append(l[i])
                if ((i < len(l) - 1) and l[i + 1] == '0' and l[i] != '0'):
                    n = l[i]
                    printafecha(n, lista)
    n = int(lista[len(lista)-1])
    printafecha(n,lista)


    return lista



n = int(input())  # Numero de casos

for i in range(1,n+1):
    l = input()
    print("Case #{}: {}".format(i,"".join(adicionaParenteses(l))))