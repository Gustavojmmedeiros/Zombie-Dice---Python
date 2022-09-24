from random import random, randint, shuffle
from collections import Counter
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
  
  for jogador in jogadores:
    ordem.append(jogador['nome'])
  
  return ordem


def pegar_dados_verdes():
  return ("C", "P", "C", "T", "P", "C")


def pegar_dados_amarelos():
  return ("T", "P", "C", "T", "P", "C")


def pegar_dados_vermelhos():
  return ("T", "P", "T", "C", "P", "T")
  

def criar_tubo_dados(tubo):
  for d in range(6):
    tubo.append(pegar_dados_verdes())
  
  for d in range(4):
    tubo.append(pegar_dados_amarelos())

  for d in range(3):
    tubo.append(pegar_dados_vermelhos())

  return tubo


# Função que sorteia e adiciona os dados à lista dos dados sorteados 
def pegar_dados(copo):  
  if len(copo) == 0:
    print('Copo vazio')
    
    for i in range(3):
      tamanho_tubo = len(tubo) - 1
      num_sorteado = randint(0, tamanho_tubo)
      dado = tubo[num_sorteado]
      copo.append(dado)
      tubo.remove(dado)
      del num_sorteado

  if len(copo) == 1:
    for i in range(2):
      tamanho_tubo = len(tubo) - 1 
      num_sorteado = randint(0, tamanho_tubo)
      dado = tubo[num_sorteado]
      copo.append(dado)
      tubo.remove(dado)
      del num_sorteado

  if len(copo) == 2:
    tamanho_tubo = len(tubo) - 1
    num_sorteado = randint(0, tamanho_tubo)
    dado = tubo[num_sorteado]
    copo.append(dado)
    tubo.remove(dado)

  return copo

        
def mostrar_dados_copo(copo):
  for dado in copo:
    if dado == ("C", "P", "C", "T", "P", "C"):
      dado = 'Verde'
    elif dado == ("T", "P", "C", "T", "P", "C"):
      dado = 'Amarelo'
    elif dado == ("T", "P", "T", "C", "P", "T"):
      dado = 'Vermelho'
  
  print(copo)


def rolar_dados(copo):
  cerebros = tiros = passos = 0
  for dado in copo:
    face_sorteada = randint(0, 5)
    if 'cerebros' and 'tiros' and 'passos' in jogador:
      if dado[face_sorteada] == 'C':
        cerebros += 1
        print('Cérebro!', end=' ')
      elif dado[face_sorteada] == 'T':
        tiros += 1
        print('Tiro!', end=' ')
      elif dado[face_sorteada] == 'P':
        passos += 1
        print('Vítima fugiu!', end=' ')
  # print(f'{cerebros} cérebros, {tiros} tiros e {passos} passos')
  return cerebros, tiros, passos
  

def mostrar_score(jogadores, jogador):
  for jogador in jogadores:
    print(f'{jogador["nome"]}: {jogador["cerebros"]} cérebros, {jogador["tiros"]} tiros')


def checar_vitoria(cerebros):
  if cerebros < 13:
    print(f'{cerebros} cérebros.')
  else:
    print('Você comeu 13 cérebros. Parabéns!')


def passar_turno(jogador_atual):
  jogador_atual += 1
  if jogador_atual >= numero_jogadores:
    jogador_atual = 0
  return jogador_atual


def jogar():
  print()
  print('*** OPÇÕES ***')
  print('1. Mostrar score')
  print('2. Rolar dados')
  print('3. Passar turno')
  
  op = int(input('Escolha uma das ações: \n'))
  if 1 <= op <= 3:
    return op
  else:
    print('Ação inválida.')


# jogada
jogadores = []
jogador = {'nome': '', 'index': 0, 'cerebros': 0, 'tiros': 0, 'passos': 0}

tubo = []
copo = []

print('Vamos jogar Zombie Dice!\n')
numero_jogadores = int(input('Quantos jogadores? '))
guardar_nome_jogador(numero_jogadores)
jogador_atual = 0

print(f'\nA ordem de jogadas é: ')
ordem_jogadas = ordem_jogo(jogadores)
criar_tubo_dados(tubo)

for c in range(len(ordem_jogadas)):
  print(f'{c + 1}º: {ordem_jogadas[c]}')

turno = True

while (turno):
  print(f'\nJogador atual: {jogadores[jogador_atual]["nome"]}\n')

  op = jogar()
  if op == 1:
    mostrar_score(jogadores, jogador)

  elif op == 2:
    pegar_dados(copo)
    mostrar_dados_copo(copo)
    
    c, t, p = rolar_dados(copo)
    # print(f'{c} cérebros, {t} tiros e {p} passos')
    jogadores[jogador_atual]['cerebros'] += c
    jogadores[jogador_atual]['tiros'] += t
    jogadores[jogador_atual]['passos'] += p
    print(jogador['cerebros'])
    print(jogador['tiros'])
    print(jogador['passos'])

    

  elif op == 3:
    continuar_jogada = input('Continuar ou passar turno? [S - continuar turno /N - passar jogada] ')
    if continuar_jogada == "s" or continuar_jogada == "sim":
      pass
    else:
      turno = False
      # Aqui deve-se zerar as variáveis que contam cérebros, tiros e passos para o próximo jogador
      jogador_atual = passar_turno(jogador_atual)
      turno = True
    pass
  else:
    break
  