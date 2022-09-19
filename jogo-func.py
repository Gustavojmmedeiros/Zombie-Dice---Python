from operator import index, truediv
from random import random, randint, shuffle


def mostrar_score(jogadores, jogador):
  for jogador in jogadores:
    print(f'{jogador["nome"]}: {jogador["cerebros"]} cérebros, {jogador["tiros"]} tiros')


# Função que recebe o número de jogadores e os adiciona à lista jogadores
def guardar_nome_jogador(numero_jogadores):
  for i in range(numero_jogadores):
    jogador['nome'] = str(input(f'Nome do jogador {i + 1}: '))
    jogador['index'] = i + 1
    jogadores.append(jogador.copy())
    
  return jogadores


# Função que cria e imprime a ordem de jogo
def ordem_jogo(jogadores):
  shuffle(jogadores)

  ordem = []
  print(f'A ordem de jogadas é: ')
  
  for jogador in jogadores:
    ordem.append(jogador['nome'])

  for c in range(len(ordem)):
    print(f'{c + 1}º: {ordem[c]}')


# Função que sorteia e adiciona os dados à lista dos dados sorteados 
def pegar_dados():
  dado_verde = 'CPCTPC'
  dado_amarelo = 'TPCTPC'
  dado_vermelho = 'TPTCPT'

  tubo_dados = [
    dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_verde,
    dado_amarelo, dado_amarelo, dado_amarelo, dado_amarelo,
    dado_vermelho, dado_vermelho, dado_vermelho
  ]

  dados_sorteados = []

  for i in range(3):
    num_sorteado = randint(0, len(tubo_dados))
    dado = tubo_dados[num_sorteado]
    if dado == dado_verde:
      cor_dado = 'Verde'
    elif dado == dado_amarelo:
      cor_dado = 'Amarelo'
    elif dado == dado_vermelho:
      cor_dado = 'Vermelho'
    
    dados_sorteados.append(cor_dado)
    del tubo_dados[num_sorteado]
  
  return dados_sorteados, dado


def rolar_dados(dados_sorteados, dado):
  cerebros = 0
  tiros = 0
  passos = 0

  for jogada in range(3):
    face_sorteada = randint(0, 5)
    if dado[face_sorteada] == 'C':
      cerebros += 1
      # jogador['cerebros'] = cerebros
    elif dado[face_sorteada] == 'T':
      tiros += 1
      # jogador['tiros'] = tiros
    elif dado[face_sorteada] == 'P':
      passos += 1
      # jogador['passos'] = passos

  return cerebros
  


def jogada():
  print('*** OPÇÕES ***')
  print('1. Mostrar score')
  print('2. Pegar dados')
  print('3. Passar o turno')
  op = int(input('Escolha um das ações: '))
  if 1 <= op <= 3:
    return op
  else:
    print('Ação inválida.')


def inicio_jogo(jogadores: dict): 
  print('Vamos jogar Zombie Dice!\n')
  numero_jogadores = int(input('Quantos jogadores? '))
  guardar_nome_jogador(numero_jogadores)
  ordem_jogo(jogadores)
  

  while True:
    op = jogada()
    if op == 1:
      mostrar_score(jogadores, jogador)
    if op == 2:
      copo, dado = pegar_dados()
      x1, x2 = rolar_dados(copo, dado)
    if op == 3:
      pass
    else:
      break

  # score = {'cerebros': 0, 'tiros': 0}
  # dadosSorteados = []
  # jogadorAtual = ''


  # jogar = True
  # while jogar:
  #   turno = True

  #   while turno:
  #     jogadorAtual = jogadores[0]['nome']
  #     print(f'Turno de {jogadorAtual}')


  #     continuarTurno = str(input('Deseja continuar jogando? [S/N] '))
  #     if continuarTurno in 'Nn':
  #       jogar = False
  #       # checarScore()
  #       trocarTurno(continuarTurno)

if __name__ == '__main__':
  jogadores = []
  jogador = {'nome': '', 'index': 0, 'cerebros': 0, 'tiros': 0, 'passos': 0}
  inicio_jogo(jogadores)