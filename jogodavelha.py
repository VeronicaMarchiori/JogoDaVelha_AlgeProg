#Imprimir o estado atual do tabuleiro
def printar_tabuleiro(tabuleiro):
    for i in range(3):
        for j in range(3):
            if j < 2:
                print(tabuleiro[i][j], end=" | ")  #Se não for a última coluna, imprime o valor e depois " | "
            else:
                print(tabuleiro[i][j], end="")  #Se for a última coluna, imprime só o valor
        print()
        if i < 2:  #Se não for a última linha, imprime uma linha de separação
            print("-" * 9)
    print('\n')

#Função que verifica se teve um ganhador
def verificar_ganhador(tabuleiro, jogador): 
    #Verificar nas linhas
    for i in range(3):
        ganhou = True
        for j in range(3):
            if tabuleiro[i][j] != jogador:
                ganhou = False
                break
        if ganhou:
            return True
    #verificar nas colunas
    for i in range(3):
        ganhou = True
        for j in range(3):
            if tabuleiro[j][i] != jogador:
                ganhou = False
                break
        if ganhou:
            return True

    #Pra Verificar nas diagonais
    ganhou = True
    for i in range(3):
        if tabuleiro[i][i] != jogador:
            ganhou = False
            break
    if ganhou:
        return True
    ganhou = True
    for i in range(3):
        if tabuleiro[i][2 - i] != jogador:
            ganhou = False
            break
    if ganhou:
        return True
    return False

#Função que verifica se deu velha
def deu_velha(tabuleiro):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                return False
    return True

#Função principal
def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]  # Inicializa o jogo fazendo uma matriz com espaços em branco
    jogador_atual = "X"  #X sempre começa o jogo
    print('Olá! Bem vindo ao jogo da velha ---- Por Veronica \nO X começa, utilize numeros para escolher as posições conforme indicado a seguir:\n0: 0 | 1 | 2\n1: 0 | 1 | 2\n2: 0 | 1 | 2')
    while True:
        printar_tabuleiro(tabuleiro)
        l = int(input(f"{jogador_atual}, escolha a linha (0, 1, 2): "))
        c = int(input(f"{jogador_atual}, escolha a coluna (0, 1, 2): "))
        print('\n')

        if tabuleiro[l][c] == " ":
            tabuleiro[l][c] = jogador_atual
        else:  #Coloquei pra evitar que os jogadores coloquem as jogadas na mesma posição
            print("Essa posição já está ocupada.")
            continue
        if verificar_ganhador(tabuleiro, jogador_atual):
            printar_tabuleiro(tabuleiro)
            print(f"{jogador_atual} Ganhouuu! Parabéns")
            break
        if deu_velha(tabuleiro):
            printar_tabuleiro(tabuleiro)
            print("Deu velha!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X" #Pra alternar os jogadores

jogar()