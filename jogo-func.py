from random import random, randint, shuffle

jogadores = []
jogador = {'nome': '', 'index': 0, 'cerebros': 0, 'tiros': 0, 'passos': 0}

# for i in range(3):
#   jogador['nome'] = str(input(f'Nome do jogador {i + 1}: '))
#   jogador['index'] = i + 1
#   jogador['cerebros'] = 0
#   jogador['tiros'] = 0
#   jogador['passos'] = 0
#   jogadores.append(jogador.copy())

for i in range(3):
  jogador['nome'] = str(input(f'Nome do jogador {i + 1}: '))
  jogador['index'] = i + 1
  jogadores.append(jogador.copy())

# Jogada
shuffle(jogadores)
jogador1 = jogadores[0]
jogador2 = jogadores[1]
jogador3 = jogadores[2]
print(jogadores)

cerebros = 0
tiros = 0
passos = 0
dadosSorteados = []
jogadorAtual = ''

dadoVerde = 'CPCTPC'
dadoAmarelo = 'TPCTPC'
dadoVermelho = 'TPTCPT'

tuboDados = [
  dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
  dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo,
  dadoVermelho, dadoVermelho, dadoVermelho
]



def pegarDados(tuboDados):
  jogadorAtual = jogador1
  print(jogador1['nome'])

  for i in range(1, 4):
    numSorteado = randint(0, 12)
    global dado
    dado = tuboDados[numSorteado]
    if dado == dadoVerde:
      corDado = 'Verde'
    elif dado == dadoAmarelo:
      corDado = 'Amarelo'
    elif dado == dadoVermelho:
      corDado = 'Vermelho'
    
    dadosSorteados.append(corDado)
    del tuboDados[numSorteado]


  global dado1 
  dado1 = dadosSorteados[0]
  global dado2
  dado2 = dadosSorteados[1]
  global dado3
  dado3 = dadosSorteados[2]

  if dado1 == dado2 == dado3:
    print(f'3 dados {dado1}s.')
  if dado1 == dado2 != dado3:
    print(f'2 dados {dado1}s e 1 dado {dado3}.')
  if dado1 != dado2 == dado3:
    print(f'1 dado {dado1} e 2 dados {dado2}s.')
  if dado1 != dado2 != dado3:
    print(f'1 dado {dado1}, 1 dado {dado2} e 1 dado {dado3}.')

  return dado1, dado2, dado3
    


def mostrarDadosTubo(dado1, dado2, dado3):
  return tuboDados



def lancarDados():
  for jogada in range(3):
    faceSorteada = randint(0, 6)

  if dado[faceSorteada] == 'C':
    cerebros += 1
    # jogador['cerebros'] = cerebros
  elif dado[faceSorteada] == 'T':
    tiros += 1
    # jogador['tiros'] = tiros
  elif dado[faceSorteada] == 'P':
    passos += 1
    # jogador['passos'] = passos



def mostrarDadosSelecionados():
  print(dado1, dado2, dado3)



def comecarTurno(tuboDados):
  pass

def passarTurno():
 pass


def checarScore():
  pass



pegarDados(tuboDados)
