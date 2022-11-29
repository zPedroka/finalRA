preco = float(input("digite o preco antigo do jogo:"))

if preco <= 20.0:
    preconovo = preco * 1.05
elif 20.0 < preco <= 80.0:
    preconovo = preco * 1.10
elif preco > 80.0:
    preconovo = preco * 1.15

if preconovo <= 40.0:
    mensagem = "Barato"
elif 40.0 < preconovo <= 80.0:
    mensagem = "Normal"
elif 81.0 < preconovo <= 120.0:
    mensagem = "Caro"
elif preconovo > 120.0:
    mensagem = "Muito caro"
    
print(f"O novo valor do jogo sera {preconovo:.2f} e esta:{mensagem}")

