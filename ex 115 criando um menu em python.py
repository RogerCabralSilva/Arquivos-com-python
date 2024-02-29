import uteis

print(uteis.cabeçalho())

while True:
    print(uteis.menu(["Ver pessoas cadastradas", "Cadastrar nova Pessoa", "Sair do programa"]))
    while True:
        try:
            opcao = int(input("Sua opção: ", ))
        except:
            print("  ERRO: por favor, digite um número inteiro válido")
            continue
        break
    if opcao == 1:
        print(uteis.opcao_1())
        print("")
        uteis.abrirArquivo()
        print("")
    elif opcao == 2:
        print(uteis.opcao_2())
        uteis.CriarArquivo()
        uteis.linhas()
    elif opcao == 3:
        break
    else:
        print("\nValor digitado inexistente.")
  