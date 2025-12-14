usuarios = {}

while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Buscar usuário")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")

        if nome in usuarios:
            print("Usuário já cadastrado!")
        else:
            idade = int(input("Idade: "))
            profissao = input("Profissão: ")

            usuarios[nome] = {
                "idade": idade,
                "profissao": profissao
            }

            print("Usuário cadastrado com sucesso!")
            

    elif opcao == "2":
        if not usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            for nome, dados in usuarios.items():
                print(f"\nNome: {nome}")
                print(f"Idade: {dados['idade']}")
                print(f"Profissão: {dados['profissao']}")

    elif opcao == "3":
        nome = input("Digite o nome do usuário: ")

        if nome in usuarios:
            print(f"\nNome: {nome}")
            print(f"Idade: {usuarios[nome]['idade']}")
            print(f"Profissão: {usuarios[nome]['profissao']}")
        else:
            print("Usuário não encontrado.")

    elif opcao == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")
