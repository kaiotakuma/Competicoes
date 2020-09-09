def printaparenteses(n,lista):

    for i in range(int(n)):
        lista.append(')')
def printaAbre(n,lista):
    for i in range(int(n)):
        lista.append('(')


def adicionaParenteses(l):
    lista = []
    for i in range(len(l)):

        if((i < len(l) -1 ) and (int(l[i]) > int(l[i+1]))):
            if ((i > 0) and (l[i - 1] == l[i])):
                lista.append(l[i])
            else:
                printaAbre(l[i],lista)
                lista.append(l[i])
                if (l[len(l) - 1] != '0' and i == len(l) - 1):
                    k = l[len(l) - 1]
                    printaparenteses(k, lista)


        elif l[i] == '0' and i != 0:
            ult_valor = lista[len(lista) - 1]
            printaparenteses(ult_valor,lista)
            if(l[i-1] != '0'):
                lista.append('0')
            else:
                lista.append('0')
        elif(l[i] == '0'):
            lista.append('0')
        else:
            if((i > 0) and (l[i-1] == l[i])):
                lista.append(l[i])
            else:
                lista.append('(')
                lista.append(l[i])
                if(l[len(l) - 1] != '0' and i == len(l) - 1):
                    k = l[len(l) - 1]
                    printaparenteses(k,lista)

    return lista



n = int(input())  # Numero de casos

for i in range(1,n+1):
    l = input()
    print("Case #{}:{} ".format(i,"".join(adicionaParenteses(l))))