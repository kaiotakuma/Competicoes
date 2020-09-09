def melhorCaso(lista,d,n):
    casos00= []
    aux = 0
    for i in range(n-1,-1,-1):
        if(i == n-1):
            incremento = 1
            while(aux <= d):
                casos00.append(aux)  # Ordem do menor para o maior
                aux = lista[i]* incremento
                incremento = incremento + 1

            maior = max(casos00)
            casos00.clear()
            aux =0
        elif(i == 0):
            casos00.clear()
            aux = 0
            incremento = 1
            while (aux <= d):
                casos00.append(aux)  # Ordem do menor para o maior
                aux = lista[i] * incremento
                incremento = incremento + 1

            maioraux = maior
            maior = max(casos00)
            if(maior <= d and maior <=maioraux):
                return  maior
            else:
                while(maior > d or maior > maioraux):#até o antessor ser menor igual
                    casos00.remove(maior)
                    maior = max(casos00)
                return maior
        else:
            casos00.clear()
            incremento = 1
            aux =0
            while (aux <= d):
                casos00.append(aux)  # Ordem do menor para o maior
                aux = lista[i] * incremento
                incremento = incremento + 1

            maioraux = maior
            maior = max(casos00)
            if(maior <= d and maior <=maioraux):
                a = True
            else:
                while(maior > d or maior > maioraux):#até o antessor ser menor igual
                    casos00.remove(maior)
                    maior = max(casos00)

    return maior

#Entrada

t = int(input()) # numero de testes

for i in range(t):
    nd = (list(map(int,input().split())))

    l = (list(map(int,input().split())))
    x = melhorCaso(l,nd[1],nd[0])
    print("Case #{}: {}".format(i+1,x))
