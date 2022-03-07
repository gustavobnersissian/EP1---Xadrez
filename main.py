import chess
import time
from random import randint

# 0(usuario); 1(programa) > rodada:impar(programa), par(usuario)
rodada = 0
ultimoMov = None #variavel usada pra saber quem fez o ultimo movimento e definir quem ganhou 
board = chess.Board()
#posicao = 0


def minimax(posicao, depth, maximizing_player): #table is board 
  posicao = list(board.legal_moves)
  #teste = str(posicao)
  if depth == 0 or posicao.is_game_over(): #don't go deeper if game over/depth ended 
    return eval(posicao)
    
  elif maximizing_player == True: 
    best_value = -1000 
    for pos in posicao: 
      value = max(best_value, minimax(pos, depth -1, False))
      if value > best_value :
        best_value = max(best_value, value)
    return best_value
    
  else:
    worst_value = +1000
    for pos in posicao: 
      value = min(worst_value, minimax(pos, depth -1, True))
      if value > worst_value :
        worst_value = min(worst_value, value)
    return worst_value

Heuristica = ["b6", "g6","a7","b7","c7","d7","e7", "f7", "g7", "h7","c5", "c6", "d5", "d6", "e5", "e6", "f5", "f6"] #lista com posicoes centralizadas do lado de cima do tabuleiro

class Xadrez:
  def __init__(self):
    self.estado = None

  # def inicializar(self):
  #   estado = chess.Board()
  #   self.estado = estado

  def VezUsuario(): #funcao da vez do usuario de jogar
    legalMoves = list(board.legal_moves) #variavel que guarda como lista os movimentos possíveis
    print("Seus Movimentos Possíveis: ")
    # legal_moves retorna as todas as possíveis jogadas
    print(list(board.legal_moves)) #mostra os movimentos possíveis   
    print("Exemplo de jogada: x1x2 (x1 = posição atual; x2 = nova posição)") #mostra como o usuario deve digitar o movimento
    #print("Exemplo de jogada se o peão for chegar na linha 1 ou 8: x1x2X (x1= posição atual; x2 = nova posição; X = Letra da peça de substituição: Q = rainha, R = torre, N = cavalo, B = bispo)")
    movimento = input("Sua vez! Qual seu movimento?\n") #pede para o usuario escolher um movimento
    #print(movimento.lower())
    for item in range(0,len(legalMoves)): #percorre a lista legalMoves 
      #print(legalMoves[item])
      if movimento.lower() == str(legalMoves[item]): #se a jogada do usuario for um movimento possivel
        board.push_san(movimento.lower()) #função que move a peça
        teste_string = str(movimento.lower())
        return teste_string #sai dessa funcao
        
    print("ERRO: Movimento inválido!\n")
    Xadrez.VezUsuario()#chama a função VezUsuario() denovo, pois a jogada do usuario não era possivel
    #novaString = str(movimento)
    #end = 3
    
    
    #if novaString[1:end-1] == "x" :
      #print("Você eliminou uma peça adversária!")
    
  def turno(rodada): #funcao para ver de quem é a vez, se "n" for 0 é a vez do programa, se for 1 é a vez do usuario
    n = rodada % 2
    if n == 0:
      return 0
    else:
      return 1

  def jogar(posicao): #funcao da jogada do programa
    
    #print(board.legal_moves)
    legalMoves = list(board.legal_moves) #variavel que guarda como lista os movimentos possíveis
    #print(legalMoves)
    # if rodada == 7:
    #   print(rodada)
    #   print("rodada minimax")
    if rodada < 10: #se o valor da rodada for menor q 10
      jogou = False #variavel pra saber se o programa ja jogou
      mov = randint(0, len(legalMoves)-1) #variavel que guarda um valor aleatorio de 0 até a quantidade de movimentos possíveis -1
      #print(mov)
      jogada = str(legalMoves[mov]) #variavel q guarda como string o movimento do programa
      #print(jogada[2:])
      #print(Heuristica[0])
      for item in range(0,len(Heuristica)): #percorre a lista Heuristica
        if jogada[2:] == Heuristica[item] and jogou == False: #se a jogada do programa for uma das jogadas da Heuristica e programa ainda n jogou
          board.push_san(jogada) #faz a jogada 
          jogou = True #variavel pra saber se o programa ja jogou     
          print("Vez do Programa!")
          print(jogada) #mostra a jogada do programa
          return
      if jogou == False: #se o programa ainda nao jogou
        Xadrez.jogar(posicao) #chama a funcao jogar pra escolher outra jogada
    #end = None
    else: #se o valor da rodada' é maior ou igual a 10

      #FUNÇÃO MELHOR JOGADA
        time.sleep(5)
        parcial = posicao[2:] 
        jogou = False
        cont = 0
        for index, item in enumerate(legalMoves):
          parcial2 = str(item)
          if parcial in parcial2:
            if cont == 0:
              cont = 1
              jogou = False
              jogada_ataque = chess.Move.from_uci(parcial2)
              board.push(jogada_ataque)
              jogou = True
              print("Vez do Programa!")
              print(jogada_ataque)
            #board.push_san(parcial)     
  
        if jogou == False:
          jogou = False 
          mov = randint(0, len(legalMoves)-1) 
          jogada = str(legalMoves[mov])
          board.push_san(jogada)
          jogou = True   
          print("Vez do Programa!")
          print(jogada)


# MAIN          
      
print(board, "\n") #mostra o tabuleiro no estado inicial  
#Xadrez.minimax(board, 4 , True, -9999, +9999)
while(board.is_game_over() == False): #roda enquanto Fim de jogo é falso, ou seja, nao acabou a partida 

  retorno = Xadrez.VezUsuario()#jogada do usuario
  print(board, "\n")
  Xadrez.jogar(retorno) #jogada do programa
    
  print(board,"\n") #mostra o tabuleiro atualizado depois de cada jogada
  ultimoMov = Xadrez.turno(rodada) #variavel que recebe valor 0 ou 1, sendo 0 se a ultima jogada foi do programa, e 1 se foi do usuario
  rodada = rodada + 1 #linha para alternar os turnos
  
if board.is_checkmate() == True: #se deu checkmate
  if ultimoMov == 1: #se o ultimo movimento foi do programa
    print("Vitória Do Programa")
  else: #se o ultimo movimento foi do usuario
    print("Vitória Do Usuário")

else: #se nao deu checkmate
  if board.is_stalemate() == True or board.is_insufficient_material() == True: #se rei nao tem mais movimento ou nao tem pecas suficientes pra dar checkmate
    print("Empate")

  
print("\nGG")