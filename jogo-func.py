from random import random, randint, shuffle


def mostrar_score(jogadores, jogador):
  for jogador in jogadores:
    print(f'{jogador["nome"]}: {jogador["cerebros"]} cérebros, {jogador["tiros"]} tiros')


# Função que recebe o número de jogadores e os adiciona à lista jogadores
def guardar_nome_jogador(numero_jogadores):
  for i in range(numero_jogadores):
    jogador['nome'] = str(input(f'Nome do jogador {i + 1}: \n'))
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
      tamanho_tubo = len(tubo)
      print(tamanho_tubo)
      num_sorteado = randint(0, tamanho_tubo)
      dado = tubo[num_sorteado]
      copo.append(dado)
      tubo.remove(dado)
      del num_sorteado

  if len(copo) == 1:
    for i in range(2):
      tamanho_tubo = len(tubo)
      print(tamanho_tubo)
      num_sorteado = randint(0, tamanho_tubo)
      dado = tubo[num_sorteado]
      copo.append(dado)
      tubo.remove(dado)
      del num_sorteado

  if len(copo) == 2:
    tamanho_tubo = len(tubo)
    print(tamanho_tubo)
    num_sorteado = randint(0, tamanho_tubo)
    dado = tubo[num_sorteado]
    copo.append(dado)
    tubo.remove(dado)

  return copo

        
def mostrar_dados_copo(copo):
  copo_jogador = []

  for dado in copo:
    if dado == ("C", "P", "C", "T", "P", "C"):
      copo_jogador.append(pegar_dados_verdes())
    elif dado == ("T", "P", "C", "T", "P", "C"):
      copo_jogador.append(pegar_dados_amarelos())
    elif dado == ("T", "P", "T", "C", "P", "T"):
      copo_jogador.append(pegar_dados_vermelhos())
  
  print(copo_jogador)


def rolar_dados(copo_jogador):
  for dado in copo_jogador:
    for i in range(3):
      face_sorteada = randint(0, 5)
      if dado[face_sorteada] == 'C':
        cerebros += 1
        print('Cérebro')
      elif dado[face_sorteada] == 'T':
        tiros += 1
        print('Tiro')
      elif dado[face_sorteada] == 'P':
        passos += 1
        print('Vítima fugiu')


def jogar():
  print()
  print('*** OPÇÕES ***')
  print('1. Mostrar score')
  print('2. Pegar dados')
  print('3. Rolar dados')
  print('4. Passar o turno')
  
  op = int(input('Escolha uma das ações: '))
  if 1 <= op <= 4:
    return op
  else:
    print('Ação inválida.')


def passar_turno(jogador_atual):
  jogador_atual += 1
  if jogador_atual >= numero_jogadores:
    jogador_atual = 0
  return jogador_atual


# jogada
jogadores = []
jogador = {'nome': '', 'index': 0, 'cerebros': 0, 'tiros': 0}

tubo = []
copo = []
cerebros = 0
tiros = 0
passos = 0

print('Vamos jogar Zombie Dice!\n')
numero_jogadores = int(input('Quantos jogadores? '))
guardar_nome_jogador(numero_jogadores)
jogador_atual = 0

turno = True

while jogar():
  while (turno):
    print(f'\nA ordem de jogadas é: ')
    ordem_jogadas = ordem_jogo(jogadores)
    for c in range(len(ordem_jogadas)):
      print(f'{c + 1}º: {ordem_jogadas[c]}')

    print(f'Jogador atual: {jogador_atual}')

    op = jogar()
    if op == 1:
      mostrar_score(jogadores, jogador)

    if op == 2:
      criar_tubo_dados(tubo)
      pegar_dados(copo)
      mostrar_dados_copo(copo)

    if op == 3:
      pass

    if op == 4:
      continuar_jogada = input('Continuar ou passar turno? [S - continuar turno /N - passar jogada] ')
      if continuar_jogada == "s" or continuar_jogada == "sim":
        pass
      else:
        turno = False
        jogador_atual = passar_turno(jogador_atual)
        turno = True
      pass
    else:
      break
    # continuar op = 2 aqui