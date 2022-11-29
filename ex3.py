nomes = []
idade = []
telefone = []
emails = []
for usuario in range(3):
    nome = input("Nome do usuario:")
    nomes.append(nome)
    ano = int(input("Ano de nascimento:"))
    idadeatual = 2022 - ano
    idade.append(idadeatual)
    tel = input("telefone:")
    telefone.append(tel)
    email = input("email:")
    emails.append(email)
    
print("------ lista de usuarios -------")
print(f"USUARIO 1\nNome:{nomes[0]}\nIdade:{idade[0]}\nTelefone:{telefone[0]}\nEmail:{emails[0]}")
print("-------------------------------")
print(f"USUARIO 2\nNome:{nomes[1]}\nIdade:{idade[1]}\nTelefone:{telefone[1]}\nEmail:{emails[1]}")
print("-------------------------------")
print(f"USUARIO 3\nNome:{nomes[2]}\nIdade:{idade[2]}\nTelefone:{telefone[2]}\nEmail:{emails[2]}")