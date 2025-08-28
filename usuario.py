print("------------SISTEMA DE USUÁRIOS---------------------")
print("BEM VINDO...")

usuario = []

while True:
    
    print("1 - Cadastrar usuário: ")
    print("2 - Listar usuários: ")
    print("3 - Remover usuário: ")
    print("0 - Sair do programa: ")

    opcao = input("Digite a opção: ")

    if opcao == "1":
        novo_usuario = input("Digite um novo usuario: ")
        usuario.append(novo_usuario)
        print(f"{novo_usuario} Adicionado com sucesso")
    elif opcao == "2":
        for i, usuarios in enumerate(usuario, start=1):
            print(f"{i}. {usuarios}")
    elif opcao == "3":
        remover_usuario = input("Digite o nome do usuário: ")
        usuario.remove(remover_usuario)
        print(f"{remover_usuario} removido com sucesso !")
    elif opcao == "0":
        break