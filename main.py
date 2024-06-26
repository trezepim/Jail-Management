riscos = ["Risco Baixo", "Risco Médio", "Risco Alto"]
detentos = ["Pedro", "João", "Vazio"]

matriz = []

tamanho = 3


def criarMatriz():
    for l in range(tamanho):
        linha = []
        for c in range(tamanho):
            elemento = " "
            linha.append(elemento)
        matriz.append(linha)
    matriz[0][0] = "X"
    matriz[1][2] = "X"


def printRiscos():
    global stringFormatada
    riscosFormatado = []
    for elemento in riscos:
        if elemento == riscos[0]:
            riscosFormatado.append(f"{elemento:>17}")
        else:
            riscosFormatado.append(f"{elemento:>12}")
    stringFormatada = " ".join(riscosFormatado)


def printMatriz():
    print("\n")
    print("============================================")
    print(stringFormatada)
    for i in range(len(matriz)):
        linhaFormatada = "  ".join(f"{elemento:<11}" for elemento in matriz[i])
        print(f"{detentos[i]:<11} {linhaFormatada}")
    print("============================================")


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

    if alteracao == 1:
        alterarNomeDetento()
        print("\n" * 2)
        print("Os dados foram alterados com sucesso!")
    elif alteracao == 2:
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


def estruturaRiscoNovo():
    global indice
    global novoRisco

    for posicao in range(3):
        if matriz[indice][posicao] == "X":
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

    if alterarRisco == 1:
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
    elif alterarRisco == 2:
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
    elif alterarRisco == 3:
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


def alterarAmbos():
    alterarNomeDetento()
    if alterarDetento < 1 and alterarDetento > 3:
        alterarAmbos()

    alterarRiscoDetento()
    if alterarRisco < 1 and alterarRisco > 3:
        alterarRiscoDetento()
    if novoRisco < 1 and novoRisco > 3:
        alterarRiscoDetento()


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


def auxPesquisaRisco():
    for z in range(3):
        posicaoX = matriz[aux].index("X")
    print("\n")
    print("----------------------------------")
    print(f"O detento {detentos[aux]} tem {riscos[posicaoX]}")


def pesquisarRiscoDetento():
    global aux
    print("\n")
    print("Deseja saber o risco de qual detento?")
    print("")
    print(f"1 - {detentos[0]}")
    print(f"2 - {detentos[1]}")
    print(f"3 - {detentos[2]}")
    print("")
    escolhaDetento = int(input("> "))

    if escolhaDetento == 1:
        aux = 0
        auxPesquisaRisco()
    elif escolhaDetento == 2:
        aux = 1
        auxPesquisaRisco()
    elif escolhaDetento == 3:
        aux = 2
        auxPesquisaRisco()
    else:
        print("\n")
        print("============================================")
        print("ERRO: Número inválido, tente novamente.")
        pesquisarRiscoDetento()
    escolherFuncao()


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

        for linha in matriz:
            if linha[riscoEscolhido] == "X":
                x += 1
        print("")
        print(f"Tem {x} detentos no Risco {escolhaRisco}.")
    else:
        print("\n")
        print("============================================")
        print("ERRO: Número inválido, tente novamente.")
        pesquisaRiscos()
    escolherFuncao()


criarMatriz()
primeiroCadastro()
printRiscos()

printMatriz()
escolherFuncao()

print("")
print("-------------------------------")
print("  Mayara Hafez | Rafael Pim  ")
print("\n")
