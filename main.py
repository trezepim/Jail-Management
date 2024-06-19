# Criando os vetores
riscos = ["Risco Baixo", "Risco Médio", "Risco Alto"]
detentos = ["Pedro", "João", "Vazio"]

# Iniciando uma matriz vazia
matriz = []

# Definindo o tamanho da matriz
tamanho = 3


# Criando a matriz com os elementos
def criarMatriz():
    for l in range(tamanho):
        linha = []  # Criando uma linha vazia
        for c in range(tamanho):
            elemento = " "
            linha.append(elemento)  # Adicionando o elemento à linha
        matriz.append(linha)  # Adicionando a linha na matriz

    matriz[0][0] = "X"
    matriz[1][2] = "X"


# Função do vetor riscos para usar no print da matriz
def printRiscos():
    global stringFormatada
    riscosFormatado = []
    for elemento in riscos:
        if elemento == riscos[0]:
            riscosFormatado.append(f"{elemento:>17}")  # >17 dá espaço à esquerda
        else:
            riscosFormatado.append(f"{elemento:>12}")
    stringFormatada = " ".join(riscosFormatado)


# Printar a matriz completa
def printMatriz():
    print("\n")
    print("============================================")
    print(stringFormatada)
    for i in range(len(matriz)):
        linhaFormatada = "  ".join(f"{elemento:<11}" for elemento in matriz[i])
        print(f"{detentos[i]:<11} {linhaFormatada}")
    print("============================================")


# Função para cadastrar detento
def primeiroCadastro():
    global detento
    global risco

    print("\n")
    print("CADASTRE UM DETENTO:")
    print("-------------------")
    print("")
    print("Informe o nome do detento:")
    print("")
    detento = input("> ")

    print("")
    print(f"Digite o número correspondente ao quão perigoso é o detento {detento}.")
    print("")
    print("1 - Risco Baixo")
    print("2 - Risco Médio")
    print("3 - Risco Alto")
    print("")
    risco = int(input("> "))

    if risco == 1:
        matriz[2][0] = "X"
        detentos[2] = detento
    elif risco == 2:
        matriz[2][1] = "X"
        detentos[2] = detento
    elif risco == 3:
        matriz[2][2] = "X"
        detentos[2] = detento
    else:
        print("\n")
        print("============================================")
        print("ERRO: Número inválido, cadastre novamente!")
        primeiroCadastro()
    print("\n" * 2)
    print("Detento cadastrado com sucesso!")


# Função de alterar nome do detento
def alterarNomeDetento():
    global alterarDetento
    alterarNome = 0

    print("\n")
    print("Qual o nome do detento que deseja alterar?")
    print("")
    print(f"1 - {detentos[0]}")
    print(f"2 - {detentos[1]}")
    print(f"3 - {detentos[2]}")
    print("")
    alterarDetento = int(input("> "))
    if alterarDetento == 1:
        print("\n")
        print("Informe o nome do novo detento:")
        alterarNome = input("> ")
        detentos[0] = alterarNome
    elif alterarDetento == 2:
        print("\n")
        print("Informe o nome do novo detento:")
        alterarNome = input("> ")
        detentos[1] = alterarNome
    elif alterarDetento == 3:
        print("\n")
        print("Informe o nome do novo detento:")
        alterarNome = input("> ")
        detentos[2] = alterarNome
    else:
        print("\n")
        print("============================================")
        print("ERRO: Número inválido, tente novamente.")
        alterarMatriz()
    print("\n" * 2)
    print("O nome do detento foi alterado com sucesso!")


# Função auxiliar para alterar risco do detento
def estruturaRiscoNovo():
    global indice
    global novoRisco  # variavel indice sera indice -1 pra qual detento ele escolheu

    for posicao in range(3):  # Itera pelas 3 posições da linha do detento
        if matriz[indice][posicao] == "X":  # Encontra a posição do "X"
            if novoRisco == 1:
                matriz[indice][posicao] = " "
                matriz[indice][0] = "X"
            elif novoRisco == 2:
                matriz[indice][posicao] = " "
                matriz[indice][novoRisco - 1] = "X"
            elif novoRisco == 3:
                matriz[indice][posicao] = " "
                matriz[indice][novoRisco - 1] = "X"
            else:
                print("\n")
                print("============================================")
                print("ERRO: Número inválido, tente novamente.")
                alterarRiscoDetento()


# Função para alterar risco do detento
def alterarRiscoDetento():
    global indice
    global novoRisco
    global alterarRisco

    print("\n")
    print("Qual o detento que deseja alterar o risco?")
    print("")
    print(f"1 - {detentos[0]}")
    print(f"2 - {detentos[1]}")
    print(f"3 - {detentos[2]}")
    print("")
    alterarRisco = int(input("> "))

    if alterarRisco == 1:  # Alterar risco do detento 1
        print("\n")
        print(f"Informe o novo risco do detento {detentos[0]}")
        print("")
        print("1 - Risco Baixo")
        print("2 - Risco Médio")
        print("3 - Risco Alto")
        print("")
        novoRisco = int(input("> "))
        indice = 0
        print("\n")
        estruturaRiscoNovo()
    elif alterarRisco == 2:  # Alterar risco do detento 1
        print("\n")
        print(f"Informe o novo risco do detento {detentos[1]}")
        print("")
        print("1 - Risco Baixo")
        print("2 - Risco Médio")
        print("3 - Risco Alto")
        print("")
        novoRisco = int(input("> "))
        indice = 1
        print("\n")
        estruturaRiscoNovo()
    elif alterarRisco == 3:  # Alterar risco do detento 1
        print("\n")
        print(f"Informe o novo risco do detento {detentos[2]}")
        print("")
        print("1 - Risco Baixo")
        print("2 - Risco Médio")
        print("3 - Risco Alto")
        print("")
        novoRisco = int(input("> "))
        indice = 2
        print("\n")
        estruturaRiscoNovo()
    else:
        print("\n")
        print("============================================")
        print("ERRO: Número inválido, tente novamente.")
        alterarRiscoDetento()
    print("\n" * 2)
    print("O risco do detento foi alterado com sucesso!")


# Função para escolher o que o usuário quer fazer na matriz
def escolherFuncao():
    global escolha

    print("\n")
    print("O que deseja fazer?")
    print("")
    print("1 - Alterar dados na matriz")
    print("2 - Pesquisar dados na matriz")
    print("3 - Finalizar o programa e ver a matriz")
    print("")
    escolha = int(input("> "))

    if escolha == 1:
        alterarMatriz()
    elif escolha == 2:
        pesquisarMatriz()
    elif escolha == 3:
        printMatriz()
    else:
        print("\n")
        print("============================================")
        print("ERRO: Número inválido, escolha novamente.")
        escolherFuncao()


# Função para alterar dados na matriz
def alterarMatriz():
    alteracao = 0

    print("\n")
    print("ALTERAÇÃO DE DADOS NA MATRIZ")
    print("----------------------------")
    print("")
    print("Digite o número correspondente a qual dado deseja alterar.")
    print("")
    print("1 - Nome do detento")
    print("2 - Risco do detento")
    print("3 - Ambos")
    print("")
    alteracao = int(input("> "))

    printMatriz()

    if alteracao == 1:  # Alterar o nome do detento
        alterarNomeDetento()
        print("\n" * 2)
        print("Os dados foram alterados com sucesso!")
    elif alteracao == 2:  # Alterar o risco do detento
        alterarRiscoDetento()
        print("\n" * 2)
        print("Os dados foram alterados com sucesso!")
    elif alteracao == 3:
        alterarAmbos()
    else:
        print("\n")
        print("============================================")
        print("ERRO: Número inválido, tente novamente.")
        alterarMatriz()

    printMatriz()
    desejaAlterar()


# Função de pesquisar qual risco é tal detento
def pesquisarRiscoDetento():
    print("\n")
    print("Deseja saber o risco de qual detento?")
    print("")
    print(f"1 - {detentos[0]}")
    print(f"2 - {detentos[1]}")
    print(f"3 - {detentos[2]}")
    print("")
    escolhaDetento = int(input("> "))

    if escolhaDetento == 1:
        posicaoX = matriz[0].index("X")
        match posicaoX:
            case 0:
                print("\n")
                print("----------------------------------")
                print(f"O detento {detentos[0]} tem {riscos[0]}")
            case 1:
                print("\n")
                print("----------------------------------")
                print(f"O detento {detentos[0]} tem {riscos[1]}")
            case 2:
                print("\n")
                print("----------------------------------")
                print(f"O detento {detentos[0]} tem {riscos[2]}")

    elif escolhaDetento == 2:
        posicaoX = matriz[1].index("X")
        match posicaoX:
            case 0:
                print("\n")
                print("----------------------------------")
                print(f"O detento {detentos[1]} tem {riscos[0]}")
            case 1:
                print("\n")
                print("----------------------------------")
                print(f"O detento {detentos[1]} tem {riscos[1]}")
            case 2:
                print("\n")
                print("----------------------------------")
                print(f"O detento {detentos[1]} tem {riscos[2]}")
    elif escolhaDetento == 3:
        posicaoX = matriz[2].index("X")
        match posicaoX:
            case 0:
                print("\n")
                print("----------------------------------")
                print(f"O detento {detentos[2]} tem {riscos[0]}")
            case 1:
                print("\n")
                print("----------------------------------")
                print(f"O detento {detentos[2]} tem {riscos[1]}")
            case 2:
                print("\n")
                print("----------------------------------")
                print(f"O detento {detentos[2]} tem {riscos[2]}")
    else:
        print("\n")
        print("============================================")
        print("ERRO: Número inválido, tente novamente.")
        pesquisarRiscoDetento()
    escolherFuncao()


# Função para ver quantos detentos tem no risco escolhido
def pesquisaRiscos():
    x = 0
    print("\n")
    print("Escolha um risco para saber quantos detentos estão nele.")
    print("")
    print("1 - Risco Baixo")
    print("2 - Risco Médio")
    print("3 - Risco Alto")
    print("")
    escolhaRisco = int(input("> "))

    if escolhaRisco > 0 and escolhaRisco < 4:
        riscoEscolhido = escolhaRisco - 1

        # Conta os "X" na coluna escolhida
        for linha in matriz:
            if linha[riscoEscolhido] == "X":
                x += 1

        print(f"Tem {x} detentos no Risco {escolhaRisco}.")
    else:
        print("\n")
        print("============================================")
        print("ERRO: Número inválido, tente novamente.")
        pesquisaRiscos()
    escolherFuncao()


# Função para pesquisar dados na matriz
def pesquisarMatriz():
    print("\n")
    print("Qual pesquisa deseja fazer?")
    print("")
    print("1 - Ver qual o risco de um detento")
    print("2 - Ver quantos detentos tem determinado risco")
    print("")
    escolhaPesquisa = int(input("> "))

    if escolhaPesquisa == 1:
        pesquisarRiscoDetento()
    elif escolhaPesquisa == 2:
        pesquisaRiscos()
    else:
        print("\n")
        print("============================================")
        print("ERRO: Número inválido, tente novamente.")


# Função para alterar o nome do detento e o risco
def alterarAmbos():
    alterarNomeDetento()
    if alterarDetento < 1 and alterarDetento > 3:
        alterarAmbos()

    alterarRiscoDetento()
    if alterarRisco < 1 and alterarRisco > 3:
        alterarRiscoDetento()
    if novoRisco < 1 and novoRisco > 3:
        alterarRiscoDetento()


# Função para perguntar se deseja alterar mais algum dado
def desejaAlterar():
    conf = 0

    print("\n")
    print("Deseja alterar outro dado?")
    print("")
    print("1 - Sim")
    print("2 - Não")
    print("")
    conf = int(input("> "))
    if conf == 1:
        alterarMatriz()
        print("\n")
    elif conf == 2:
        escolherFuncao()
        print("\n")
    else:
        print("\n")
        print("============================================")
        print("Número inválido, escolha novamente.")
        desejaAlterar()


criarMatriz()
primeiroCadastro()

printRiscos()
printMatriz()

escolherFuncao()

print("")
print("-------------------------------")
print("  Mayara Hafez | Rafael Pim  ")
print("\n")
