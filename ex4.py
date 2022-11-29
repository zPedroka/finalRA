matriz = [
    [0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0]
]

for linha in range(3):
    for coluna in range(4):
        matriz[linha][coluna] = float(input("Digite um valor real:"))

somaimpares = 0

for linha in range(3):
    somaimpares += matriz[linha][1]
for linha in range(3):
    somaimpares += matriz[linha][3]

for i in range(3):
    print(matriz[i])
    
print(f"soma dos elementos das colunas impares {somaimpares}")

print(f"media aritmetica {somaimpares/6}")

matriz[0][2] = matriz[0][0] + matriz[0][1]
matriz[1][2] = matriz[1][0] + matriz[1][1]
matriz[2][2] = matriz[2][0] + matriz[2][1]

for i in range(3):
    print(matriz[i])
    