"""

  MM    M   CCCC      111  0000   22222
  MMM  MM  CC   C      11 00  00 2    22
  M MMM M CC      |||| 11 00  00      22
  M  M  M  CC   C      11 00  00    22
  M     M   CCCC      1111 0000  2222222

"""
# https://www.ic.unicamp.br/~mc102/labs/roteiro-lab10.html

import copy # importação da lib copy para aplicar o método deepcopy na lista b

################################################################################################################
def split(word): # Função split que recebe uma palavra e retorna uma lista contendo cada caractere dessa palavra
  return list(word)
################################################################################################################

################################################################################################################
def printResult(array):
  """
    Acessa cada item (sublista) da lista principal. Dentro da
    de cada sublista imprime os caracteres lado a lado pulando linha a cada sublista consultada
    (Passo final)
  """ 
  for row in array:
    for column in row:
      print(column, end = "")
    print()
################################################################################################################

################################################################################################################
# Input do Usuário
userInput = [] # Input a ser iterado

while True: # Laço responsável por verificar o tipo de input para cada linha
  line = input()
  if (line.isdigit()): # Caso ele for um dígito, pare de ler o input e obtenha o valor dessa linha
    x = eval(line) # Esse x é útil para saber quantas iterações serão realizadas
    break
  else:
    userInput.append(line)

# Fim do Input
################################################################################################################

################################################################################################################
  arrayForSublists = [] # Array para armazenar listas de listas. Cada lista no interior de arrayForSublists
  # é uma linha do input do tipo string

  for element in userInput: 
    arrayForSublists.append(element)

  b = [] # Recebe 
  
  for i in range(len(arrayForSublists)):
    b.append(split(arrayForSublists[i]))

  # item é um novo array - cópia de b - criado para ser modificado ao mesmo tempo em que se tem a matriz b
  # como parâmetro a permanecer intacto. Ou seja, nas expressões condicionais abaixo é feito o embasamento em 
  # b ao mesmo tempo em que se altera os elementos de indice [i][j] em item. 
  item = copy.deepcopy(b)
################################################################################################################


################################################################################################################
# Laço for aplicado para re-renderizar a figura atualizando a posição das bactérias (Input do Usuário) para cada ciclo
for i in range(x):
  # Aninhamento de laços for para percorrer todas as as linhas e colunas da matriz b
  # Com exceção das duas camadas externas. Isso foi feito pois sabemos que essas duas camadas são
  # imutáveis, bastando analisar somente os internos mais internos

  """
  p: Percorre
  n: Não percorre

                nnnnnnnnnnnnn
                nnnnnnnnnnnnn
                nnpppppppppnn
                nnpppppppppnn
                nnpppppppppnn
                nnpppppppppnn
                nnpppppppppnn
                nnpppppppppnn
                nnpppppppppnn
                nnpppppppppnn
                nnnnnnnnnnnnn
                nnnnnnnnnnnnn

  """
  for i in range(2, len(b) - 2):
    for j in range(2, len(b[0]) - 2):

      # Array que armazena variáveis booleanas afirmando se os itens adjacentes ao caracte de índice b[i][j]
      spacesArray = [b[i - 1][j - 1].isspace(), b[i - 1][j].isspace(), b[i - 1][j + 1].isspace(),b[i][j + 1].isspace(), b[i + 1][j + 1].isspace(), b[i + 1][j].isspace(), b[i + 1][j - 1].isspace(), b[i][j - 1].isspace()]

      # Contador de caracteres espaço vazio (" ") em volta de cada item de índice b[i][j]
      counterSpaces = 0
      for element in spacesArray:
        if element:
          counterSpaces += 1

      # Assumindo que o item não é um espaço (A bactéria existe)
      # Se o número de espaços for menor ou igual a 4 (4 ou mais vizinhos) ou maior que 7 (menos de 2 vizinhos) => Morre!      
      if ((b[i][j] == "@" and counterSpaces <= 4) or (b[i][j] == "@" and counterSpaces > 7)): item[i][j] = " "

      # Assumindo que o item é um espaço (A bactéria não existe)
      # Se o número de espaços for igual a 5 (3 vizinhos) => Renasce!
      elif (b[i][j] == " " and counterSpaces == 5): item[i][j] = "@"
  
      # Assumindo que item não é um espaço (A bactéria existe)
      # Se o número de espaços em volta for igual a 5 ou 6 (2 ou 3 vizinhos) e a bactéria existir => Sobrevive!
      elif ((b[i][j] == "@" and counterSpaces == 5) or (b[i][j] == "@" and counterSpaces == 6)): item[i][j] = "@"
      
      # Senão continua sendo um espaço vazio
      else: item[i][j] = " "

  
  printResult(item)

