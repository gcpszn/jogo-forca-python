# Projeto - Desenvolvimento do "Jogo da Forca" em Linguagem Python - Versão Final

# Importando bibliotecas necessárias
import random
from os import system, name

# Função para limpar a tela (compatível com qualquer sistema operacional)
def limpa_tela():
 
    # Se for Windows, usa o comando 'cls'
    if name == 'nt':
        _ = system('cls')
 
    # Caso contrário, usa o comando 'clear'
    else:
        _ = system('clear')

# Função responsável por desenhar a forca na tela, de acordo com as chances restantes
def display_hangman(chances):

    # Lista de estágios da forca
    stages = [  
                # estágio 6 (forca completa - o jogador perdeu)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5 
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4 
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3 
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2 
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1 
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0 
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

# Função principal que executa o jogo da forca
def game():

    # Limpa a tela no início do jogo
    limpa_tela()
    print("\nBem-vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")
    
    # Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    
    # Sorteia uma palavra aleatoriamente da lista
    palavra = random.choice(palavras)
    
    # Converte a palavra em uma lista de letras
    lista_letras_palavras = [letra for letra in palavra]
    
    # Cria o tabuleiro com "_" representando letras ainda não adivinhadas
    tabuleiro = ["_"] * len(palavra)
    
    # Define o número inicial de chances do usuário
    chances = 6
    
    # Lista para armazenar as letras já tentadas
    letras_tentativas = []
    
    # Loop principal do jogo, continua enquanto houver chances e a palavra não for adivinhada
    while chances > 0:
        
        # Mostra o desenho atual da forca
        print(display_hangman(chances))
        # Mostra o estado atual do tabuleiro
        print("Palavra: ", tabuleiro)
        print("\n")
        
        # Pede para o usuário digitar uma letra
        tentativa = input("\nDigite uma letra: ").lower()
        
        # Verifica se a letra já foi tentada
        if tentativa in letras_tentativas:
            print("Você já tentou essa letra. Escolha outra!")
            continue
        
        # Adiciona a letra na lista de tentativas
        letras_tentativas.append(tentativa)
        
        # Verifica se a letra está na palavra sorteada
        if tentativa in lista_letras_palavras:
            print("Você acertou a letra!")
            
            # Atualiza o tabuleiro revelando a letra correta
            for indice in range(len(lista_letras_palavras)):
                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa
            
            # Verifica se o usuário já completou a palavra
            if "_" not in tabuleiro:
                print(f"\nParabéns! Você venceu! A palavra era: {palavra}.")
                break
        else:
            # Letra incorreta: o jogador perde uma chance
            print("Essa letra não está na palavra!")
            chances -= 1
    
    # Se o usuário perdeu (não completou a palavra)
    if "_" in tabuleiro:
        print(display_hangman(chances))
        print(f"\nVocê perdeu! A palavra era: {palavra}.")

# Bloco Main
if __name__ == "__main__":
    game()
    print("\nParabéns! Você está aprendendo programação em Python com a DSA. :)\n")
