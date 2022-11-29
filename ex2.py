cont = 0
soma3 = 0
soma5 = 0
while cont <= 999:
    if cont % 3 == 0:
        soma3 += cont
    if cont % 5 == 0:
        soma5 += cont
    cont += 1
    
print(soma3,soma5)
