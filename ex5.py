def printamatriz():
    matriz = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    for linha in range(3):
        for coluna in range(3):
            if linha == coluna:
                print(matriz[linha][coluna])
                
lista = ["PROF"," ","Marina"," ","me passa"]

def juntanome(listapalavras):
    string = ""
    for i in range(len(listapalavras)):
        string = string + listapalavras[i]
    print (string)
    

listaint = [1,2,3,4,5,6,7,8,9,10]

def listainteiros(lista):
    listafinal = [max(lista),min(lista),sum(lista)]
    return listafinal

listaorganizada = listainteiros()
printamatriz()
juntanome(lista)
print(listaorganizada)