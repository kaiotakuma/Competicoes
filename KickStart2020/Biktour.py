def pico(lista,n):
    pico =0
    for i in range (n):# 0,1,2,3
        if(i == 0 or i == n-1):
            pico = pico +0
        else:
            if(lista[i] > lista[i-1] and lista[i] > lista[i+1]):
                pico = pico +1
            else:
                pico = pico +0
    return pico

t = int(input()) # numero de testes

for i in range(t):
    n = int(input()) # numero de elementos
    l = (list(map(int,input().split())))
    p = pico(l,n)
    print("Case #{}: {}".format(i+1,p))

