def cabeçalho(a=""):
    a = (f"""{30 * '-'}
{'MENU'.center(30)}
{30 * '-'}""")
    return a

def menu(lista):
    cont = 0
    for item in lista:
        cont += 1
        print(f"{cont} - {item}")
    return linhas()


def linhas(a=""):
    return f"{30 * "-"}"

def opcao_1(a=""):
    a = (f"""{30 * '-'}
{'OPÇÃO 1'.center(30)}
{30 * '-'}""")
    return a
    
def opcao_2(a=""):
    a = (f"""{30 * '-'}
{'OPÇÃO 2'.center(30)}
{30 * '-'}""")    
    return a

def CriarArquivo(a=""):
# Abrir o arquivo no modo 'a+' (adicionar e ler)
    with open('arquivo.txt', 'a+') as arquivo:        
        # Ler o conteúdo atual do arquivo e exibi-lo
        conteudo_atual = arquivo.read()
        print("Conteúdo atual do arquivo:")
        print(conteudo_atual)
        
        # Solicitar ao usuário para inserir o texto a ser adicionado
        nome = str(input("Nome: "))
        idade = str(input("Idade: "))
        # Adicionar o texto ao arquivo
        if nome.strip():  # Verificar se o texto não está vazio
            arquivo.write("Nome: " + nome + "\t\t")
            arquivo.write("Idade: " + idade + "\t\t")
            arquivo.write("\n")
            print("Texto adicionado ao arquivo com sucesso!\n")
            
        else:
            print("Nenhum texto adicionado.")

def abrirArquivo(a=""):
    with open('arquivo.txt', 'r') as arquivo:
        print(arquivo.read())
