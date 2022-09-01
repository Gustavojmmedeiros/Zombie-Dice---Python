# Linha de importação do módulo random 
from random import randint 

print('Prontos para jogar Zombie Dice?')
print()

print('Para iniciar, diga a quantidade de jogadores para a partida.')
print()

# Bloco de verificação da quantidade mínima e máxima de jogadores
while True:  
  quantidadeJogadores = int(input('Número de jogadores: '))
  print()
  if quantidadeJogadores >= 2:
    break
  print('O jogo permite no mínimo 2 jogadores.')

print(f'{quantidadeJogadores} jogadores selecionados.\n')

# Lista vazia para receber os jogadores
jogadores = []

for nomes in range(quantidadeJogadores):
  nomeJogador = str(input('Nome do jogador: '))
  jogadores.append(nomeJogador)

# Tipos dos dados seguido da lista com estes
dadoVerde = 'CPCTPC'
dadoAmarelo = 'TPCTPC'
dadoVermelho = 'TPTCPT'

tuboDados = [
  dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
  dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo,
  dadoVermelho, dadoVermelho, dadoVermelho
]

# Inicialização de variáveis para preenchimento ou contabilização de pontos/troca de jogadores
jogadorAtual = 0
dadosSorteados = []
cerebros = 0
tiros = 0
passos = 0

# Início do laço que permite o jogador continuar rolando os dados até tomar 3 tiros
while True:
  print(f'Turno de {jogadores[jogadorAtual]}')
  print()

  if tiros <= 3:
    jogar = str(input('Rolar dados? [S/N] ')).strip()[0]

# Validação da jogada
    if jogar in 'Nn':
      break

    else:  
      while jogar not in 'Ss':
        jogar = str(input('Rolar dados? [S/N] ')).strip()[0]
        print()

# Laço que sorteia um dado e o adiciona à lista dadosSorteados
      for i in range(1, 4):
        numSorteado = randint(0, 12)
        dado = tuboDados[numSorteado]
        if dado == dadoVerde:
          corDado = 'Verde'
        elif dado == dadoAmarelo:
          corDado = 'Amarelo'
        elif dado == dadoVermelho:
          corDado = 'Vermelho'
        
        dadosSorteados.append(corDado)

# Atribuição de cada dado para uma variável e verificação destes entre si
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

# Laço que sorteia a face sorteada do dado e qual o seu resultado
      for jogada in range(3):
        faceSorteada = randint(0, 6)

        if dado[faceSorteada] == 'C':
          cerebros += 1
        elif dado[faceSorteada] == 'T':
          tiros += 1
        elif dado[faceSorteada] == 'P':
          passos += 1

      print(f'Resultado da jogada: {cerebros} cérebros, {tiros} tiros e {passos} vítimas que fugiram.')
      print()

# Opção caso o jogador tome 3 tiros, o que encerra a sua jogada e elimina seus pontos conquistados nela
  else:
    print('Você tomou 3 ou mais tiros e perdeu sua vez! (E todos os pontos da rodada)')
    break
        
print('Até mais!')