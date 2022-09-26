from random import randint, shuffle
from time import sleep

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
    print('Copo vazio. Selecionando 3 dados...')
    
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
  print('\nDados sorteados: ', end='')
  for dado in copo:
    if dado == ("C", "P", "C", "T", "P", "C"):
      dado = 'Verde'
      print('verde', end=' ')
      # print('\033[1;32m verde\033[m', end=' ')
    elif dado == ("T", "P", "C", "T", "P", "C"):
      dado = 'Amarelo'
      print('amarelo', end=' ')
      # print('\033[1;33m amarelo\033[m', end=' ')
    elif dado == ("T", "P", "T", "C", "P", "T"):
      dado = 'Vermelho'
      print('vermelho', end=' ')
      # print('\033[1;31m vermelho\033[m', end=' ')
  print()


def rolar_dados(copo):
  print()
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

  return cerebros, tiros, passos
  

def mostrar_score(jogadores, jogador):
  for jogador in jogadores:
    print(f'{jogador["nome"]}: {jogador["cerebros"]} cérebros, {jogador["tiros"]} tiros')


def zerar_pontuacao(jogador_atual, contador_cerebros):
  c, t, p = 0, 0, 0
  jogadores[jogador_atual]['tiros'] = 0
  jogadores[jogador_atual]['passos'] = 0
  if jogadores[jogador_atual]['tiros'] >= 3:
    print('Você tomou 3 tiros! Perca sua jogada e todos os pontos feitos nela.')
  print(f'{contador_cerebros} cerebros nesta jogada')
    
  
def checar_vitoria(jogador_atual):
  if jogadores[jogador_atual]['cerebros'] >= 3:
    return True


def checar_derrota(jogador_atual):
  if jogadores[jogador_atual]['tiros'] >= 3:
    return True


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
  print('4. Sair')

  sair = False
  while not sair:
    op = int(input('Escolha uma das ações: \n'))
    if 1 <= op < 4:
      return op
    elif op == 4:
      print('Até a próxima!')
      sair = True
    else:
      print('Ação inválida.')


# jogada
jogadores = []
jogador = {'nome': '', 'index': 0, 'cerebros': 0, 'tiros': 0, 'passos': 0}

tubo = []
copo = []

print('Vamos jogar Zombie Dice!\n')
numero_jogadores = int(input('Quantos jogadores? '))
sleep(0.5)
guardar_nome_jogador(numero_jogadores)
jogador_atual = 0

print(f'\nA ordem de jogadas é: ')
sleep(0.5)
ordem_jogadas = ordem_jogo(jogadores)
criar_tubo_dados(tubo)

for c in range(len(ordem_jogadas)):
  print(f'{c + 1}º: {ordem_jogadas[c]}')

contador_cerebros = 0
contador_passos = 0
turno = True

while (turno):
  print(f'\nJogador atual: {jogadores[jogador_atual]["nome"]}\n')

  op = jogar()
  if op == 1:
    sleep(0.8)
    mostrar_score(jogadores, jogador)

  elif op == 2:
    sleep(0.8)
    pegar_dados(copo)
    mostrar_dados_copo(copo)
    
    c, t, p = rolar_dados(copo)
    contador_cerebros += c
    contador_passos += p

    jogadores[jogador_atual]['cerebros'] += c
    jogadores[jogador_atual]['tiros'] += t
    jogadores[jogador_atual]['passos'] += p
    print(f'\n{c} cérebros, {t} tiros e {p} vítimas escaparam.')

    if checar_derrota(jogador_atual):
      print('proximo jogador')
      zerar_pontuacao(jogador_atual, contador_cerebros)
      jogadores[jogador_atual]['cerebros'] -= contador_cerebros
      contador_cerebros = 0
      turno = False
      jogador_atual = passar_turno(jogador_atual)
      turno = True
    elif checar_vitoria(jogador_atual):
      sleep(0.8)
      print(f'{jogadores[jogador_atual]["nome"]} venceu! Parabéns')
      break  

  elif op == 3:
    sleep(0.8)
    continuar_jogada = input('Continuar ou passar turno? [S - continuar turno /N - passar jogada] ')
    if continuar_jogada == "s" or continuar_jogada == "sim":
      pass
    else:
      turno = False
      zerar_pontuacao(jogador_atual, contador_cerebros)
      contador_cerebros = 0
      jogador_atual = passar_turno(jogador_atual)
      turno = True
    pass

  else:
    break  