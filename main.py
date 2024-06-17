# Criando os vetores
riscos = ["Risco Baixo", "Risco Médio", "Risco Alto"]
detentos = ["Pedro", "João", "Vazio"]

# Iniciando uma matriz vazia
matriz = []

# Definindo o tamanho da matriz
tamanho = 3

risco = 0
detento = 0

alterarNome = "0"
alterarRisco = 0

conf = 0
escolha = 0
alteracao = 0

riscosFormatado = []


# Criando a matriz com os elementos
def criarMatriz():
    for l in range(tamanho):
        linha = []  # Criando uma linha vazia
        for c in range(tamanho):
            elemento = "X"
            linha.append(elemento)  # Adicionando o elemento à linha
        matriz.append(linha)  # Adicionando a linha na matriz
    # Esvaziando as células sem detento e pré selecionando os riscos
    matriz[0][1] = " "
    matriz[0][2] = " "
    matriz[1][0] = " "
    matriz[1][1] = " "
    matriz[2][0] = " "
    matriz[2][1] = " "
    matriz[2][2] = " "

# Função do vetor riscos para usar no print da matriz
def printRiscos():
    for elemento in riscos:
        if elemento == riscos[0]:
            riscosFormatado.append(f"{elemento:>17}")
        else:
            riscosFormatado.append(f"{elemento:>12}")
    stringFormatada = " ".join(riscosFormatado)
    print(stringFormatada)

# Printar a matriz completa
def printMatriz():
    print("============================================")
    printRiscos()
    for i in range(len(matriz)):
        linhaFormatada = "  ".join(f"{elemento:<11}" for elemento in matriz[i])
        print(f"{detentos[i]:<11} {linhaFormatada}")
    print("============================================")

# Função para cadastrar detento
def primeiroCadastro():
    global detento
    global risco

    print("")
    print("CADASTRE UM DETENTO:")
    print("-------------------")
    print("")
    print("Informe o nome do detento:")
    detento = input("> ")

    print("")
    print(f"Digite o número correspondente ao quão perigoso é o detento {detento}.")
    print("1 - Risco Baixo")
    print("2 - Risco Médio")
    print("3 - Risco Alto")
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
        print("")
        print("============================================")
        print("ERRO: Número inválido, cadastre novamente!")
        primeiroCadastro()

#Função de alterar nome do detento
def alterarNomeDetento():
    global alterarDetento
    
    print("")
    print("Qual o nome do detento que deseja alterar?")
    print("")
    print(f"1 - {detentos[0]}")
    print(f"2 - {detentos[1]}")
    print(f"3 - {detentos[2]}")
    alterarDetento = int(input("> "))
    if alterarDetento == 1:
        print("")
        print("Informe o nome do novo detento:")
        alterarNome = input("> ")
        detentos[0] = alterarNome
    elif alterarDetento == 2:
        print("")
        print("Informe o nome do novo detento:")
        alterarNome = input("> ")
        detentos[1] = alterarNome
    elif alterarDetento == 3:
        print("")
        print("Informe o nome do novo detento:")
        alterarNome = input("> ")
        detentos[2] = alterarNome
    else:
        print("")
        print("============================================")
        print("ERRO: Número inválido, tente novamente.")
        alterarMatriz()

#Função auxiliar para alterar risco do detento
def estruturaRiscoNovo():
    global indice
    global novoRisco   # variavel indice sera indice -1 pra qual detento ele escolheu
    
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
                print("")
                print("============================================")
                print("ERRO: Número inválido, tente novamente.")
                alterarRiscoDetento()

def alterarRiscoDetento():
    global indice
    global novoRisco
    print("")
    print("Qual o nome do detento que deseja alterar o risco?")
    print("")
    print(f"1 - {detentos[0]}")
    print(f"2 - {detentos[1]}")
    print(f"3 - {detentos[2]}")
    alterarRisco = int(input("> "))
    
    if alterarRisco == 1:  # Alterar risco do detento 1
        print("")
        print(f"Informe o novo risco do detento {detentos[0]}")
        print("1 - Risco Baixo")
        print("2 - Risco Médio")
        print("3 - Risco Alto")
        novoRisco = int(input("> "))
        indice = 0
        print("")
        estruturaRiscoNovo()
    elif alterarRisco == 2:  # Alterar risco do detento 1
        print("")
        print(f"Informe o novo risco do detento {detentos[1]}")
        print("1 - Risco Baixo")
        print("2 - Risco Médio")
        print("3 - Risco Alto")
        novoRisco = int(input("> "))
        indice = 1
        print("")
        estruturaRiscoNovo()
    elif alterarRisco == 3:  # Alterar risco do detento 1
        print("")
        print(f"Informe o novo risco do detento {detentos[2]}")
        print("1 - Risco Baixo")
        print("2 - Risco Médio")
        print("3 - Risco Alto")
        novoRisco = int(input("> "))
        indice = 2
        print("")
        estruturaRiscoNovo()
    else:
        print("")
        print("============================================")
        print("ERRO: Número inválido, tente novamente.")
        alterarRiscoDetento()
        
# Função para escolher o que o usuário quer fazer na matriz
def escolherFuncao():
    global escolha

    print("")
    print("O que deseja fazer?")
    print("")
    print("1 - Alterar dados na matriz")
    print("2 - Pesquisar dados na matriz")
    print("3 - Finalizar o programa e ver a matriz")
    escolha = int(input("> "))

    if escolha == 1:
        alterarMatriz()
    elif escolha == 2:
        pesquisarMatriz()
    elif escolha == 3:
        return printMatriz()
    else:
        print("")
        print("============================================")
        print("ERRO: Número inválido, escolha novamente.")
        escolherFuncao()

# Função para alterar dados na matriz
def alterarMatriz():
    print("")
    print("ALTERAÇÃO DE DADOS NA MATRIZ")
    print("----------------------------")
    print("Digite o número correspondente a qual dado deseja alterar.")
    print("1 - Nome do detento")
    print("2 - Risco do detento")
    print("3 - Ambos")
    print("")
    alteracao = int(input("> "))

    printMatriz()

    if alteracao == 1:  # Alterar o nome do detento
        alterarNomeDetento()
    elif alteracao == 2:  # Alterar o risco do detento
        alterarRiscoDetento()
    elif alteracao == 3:
        alterarAmbos()
    else:
        print("")
        print("============================================")
        print("ERRO: Número inválido, tente novamente.")
        alterarMatriz()

    printMatriz()
    desejaAlterar()
# Função para pesquisar dados na matriz
def pesquisarMatriz():
    print("")
    print("Deseja saber o risco de qual detento?")
    print("")
    print(f"1 - {detentos[0]}")
    print(f"2 - {detentos[1]}")
    print(f"3 - {detentos[2]}")
    escolhaDetento = int(input("> "))

    if escolhaDetento == 1:
        posicaoX = matriz[0].index("X")
        match posicaoX:
            case 0:
                print("")
                print("-------------------------------------------")
                print(f"O detento {detentos[0]} tem {riscos[0]}")
            case 1:
                print("")
                print("-------------------------------------------")
                print(f"O detento {detentos[0]} tem {riscos[1]}")
            case 2:
                print("")
                print("-------------------------------------------")
                print(f"O detento {detentos[0]} tem {riscos[2]}")
    elif escolhaDetento == 2:
        posicaoX = matriz[1].index("X")
        match posicaoX:
            case 0:
                print("")
                print("-------------------------------------------")
                print(f"O detento {detentos[1]} tem {riscos[0]}")
            case 1:
                print("")
                print("-------------------------------------------")
                print(f"O detento {detentos[1]} tem {riscos[1]}")
            case 2:
                print("")
                print("-------------------------------------------")
                print(f"O detento {detentos[1]} tem {riscos[2]}")
    elif escolhaDetento == 3:
        posicaoX = matriz[2].index("X")
        match posicaoX:
            case 0:
                print("")
                print("-------------------------------------------")
                print(f"O detento {detentos[2]} tem {riscos[0]}")
            case 1:
                print("")
                print("-------------------------------------------")
                print(f"O detento {detentos[2]} tem {riscos[1]}")
            case 2:
                print("")
                print("-------------------------------------------")
                print(f"O detento {detentos[2]} tem {riscos[2]}")
    else:
        print("")
        print("============================================")
        print("ERRO: Número inválido, tente novamente.")
        pesquisarMatriz()
    escolherFuncao()

# Função para alterar o nome do detento e o risco
def alterarAmbos():
    alterarNomeDetento()
    if alterarDetento < 1 and alterarDetento > 3:
        alterarAmbos()
        
    alterarRiscoDetento()
    if alterarRisco < 1 and alterarRisco > 3:
        alterarRiscoDetento()
    if novoRisco <1 and novoRisco > 3:
        alterarRiscoDetento()

# Função para perguntar se deseja alterar mais algum dado
def desejaAlterar():
    print("")
    print("Deseja alterar outro dado?")
    print("1 - Sim")
    print("2 - Não")
    print("")
    conf = int(input("> "))
    if conf == 1:
        alterarMatriz()
    elif conf == 2:
        escolherFuncao()
        print("")
    else:
        print("")
        print("============================================")
        print("Número inválido, escolha novamente.")
        desejaAlterar()


criarMatriz()
primeiroCadastro()

printMatriz()

escolherFuncao()

print("")
print("")
print("-------------------------------")
print("  Mayara Hafez | Rafael Pim  ")
print("")
print("")
