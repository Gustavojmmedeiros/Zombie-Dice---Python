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
jogar = str(input('Rolar dados? [S/N] '))

for i in range(1, 4):
  numSorteado = randint(0, 12)
  dado = listaDados[numSorteado]
  if dado == dadoVerde:
    corDado = 'Verde'
  elif dado == dadoAmarelo:
    corDado = 'Amarelo'
  elif dado == dadoVermelho:
    corDado = 'Vermelho'
  
  dadosSorteados.append(dado)

  print(f'{i}º dado {corDado}.')

dado1 = dadosSorteados[0]
dado2 = dadosSorteados[1]
dado3 = dadosSorteados[2]

print(dado1, dado2, dado3)
for i in range(0, 3):
  faceSorteada = randint(1, 7)

  if dado[faceSorteada] == 'C':
    print('Você devorou um cérebro.')
    cerebros += 1
  elif dado[faceSorteada] == 'T':
    print('Você tomou um tiro.')
    tiros += 1
  elif dado[faceSorteada] == 'P':
    print('Uma vítima escapou.')
    passos += 1

print(cerebros, tiros, passos)




# while True:

#   for i in range(quantidadeJogadores):
#     numSorteado = randint(0, 12)
#     dadoSorteado = listaDados[numSorteado]

#     if dadoSorteado == dadoVerde:
#       corDado = 'Verde'
#     elif dadoSorteado == dadoAmarelo:
#       corDado = 'Amarelo'
#     elif dadoSorteado == dadoVermelho:
#       corDado = 'Vermelho'
    
#   dadosSorteados.append(dadoSorteado)
  

#   break
  
# print(dadosSorteados)

#     print(f'O dado sorteado foi {corDado}.')


#   for dadoSorteado in dadosSorteados:

#     faceSorteada = randint(0, 5)

#     if dadoSorteado[faceSorteada] == 'C':
#       print('Você comeu um cérebro.')
#       cerebros += 1
#     elif dadoSorteado[faceSorteada] == 'T':
#       print('Você tomou um tiro.')
#       tiros += 1
#     elif dadoSorteado[faceSorteada] == 'P':
#       print('Você deixou uma vítima escapar.')
#       passos += 1

#   break

# print(f'Seu score atual é: {cerebros} cerebros, {tiros} tiros, {passos} vítimas que fugiram.')
