from random import randint 

print('Prontos para jogar Zombie Dice?\n')

print('Para iniciar, diga a quantidade de jogadores para a partida.\n')

quantidadeJogadores = int(input('Número de jogadores: [2/3/4/5/6]\n'))

while quantidadeJogadores < 2 or quantidadeJogadores > 6:
  print('O jogo permite no mínimo 2 e no máximo 6 jogadores.')

  quantidadeJogadores = int(input('Número de jogadores: [2/3/4/5/6]\n'))

print(f'{quantidadeJogadores} jogadores selecionados.\n')

jogadores = []

for nomes in range(quantidadeJogadores):
  nomeJogador = str(input('Nome do jogador: '))
  jogadores.append(nomeJogador)


dadoVerde = 'CPCTPC'
dadoAmarelo = 'TPCTPC'
dadoVermelho = 'TPTCPT'

listaDados = [
  dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
  dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo,
  dadoVermelho, dadoVermelho, dadoVermelho
]

jogadorAtual = 0
dadosSorteados = []
cerebros = 0
tiros = 0
passos = 0 


print(f'Turno de {jogadores[jogadorAtual]}')

jogar = str(input('Rolar dados? [S/N] ')).strip()[0]

while jogar not in 'Ss':
  jogar = str(input('Rolar dados? [S/N] ')).strip()[0]
  if jogar in 'Nn':
    break

for i in range(1, 4):
  numSorteado = randint(0, 12)
  dado = listaDados[numSorteado]
  if dado == dadoVerde:
    corDado = 'Verde'
  elif dado == dadoAmarelo:
    corDado = 'Amarelo'
  elif dado == dadoVermelho:
    corDado = 'Vermelho'
  
  dadosSorteados.append(corDado)

dado1 = dadosSorteados[0]
dado2 = dadosSorteados[1]
dado3 = dadosSorteados[2]

if dado1 == dado2 == dado3:
  print(f'3 dados {dado1}s.')
if dado1 == dado2 != dado3:
  print(f'2 dados {dado1}s e 1 dado {dado3}.')
if dado1 != dado2 == dado3:
  print(f'1 dado {dado1} e 2 dados {dado2}s.')
if dado1 != dado2 != dado3:
  print(f'1 dado {dado1}, 1 dado {dado2} e 1 dado {dado3}.')

print(dado1, dado2, dado3)

for jogada in range(3):
  faceSorteada = randint(0, 6)

  if dado[faceSorteada] == 'C':
    cerebros += 1
  elif dado[faceSorteada] == 'T':
    tiros += 1
  elif dado[faceSorteada] == 'P':
    passos += 1

print(f'Seu score atual é: {cerebros} cérebros, {tiros} tiros e {passos} vítimas que fugiram.')

