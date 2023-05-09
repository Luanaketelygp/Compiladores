alfabeto = [
    'a', 'b', 'c', 'd', 'e', 
    'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 
    'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 'z'
]
numeros = [
    '0', '1', '2', '3', '4', 
    '5', '6', '7', '8', '9'
]
padroes = ['+', '-']
dot = ['.']
automaton = {
    'q0': {
        'alfabeto': 'q0',
        'numeros': 'q1',
        'dot': 'q0',
        'operator': 'q0'
    },
    'q1': {
        'alfabeto': 'q2',
        'numeros': 'q1',
        'dot': 'q3',
        'operator': 'q2'
    },
    'q2': {
        'alfabeto': 'q2',
        'numeros': 'q2',
        'dot': 'q2',
        'operator': 'q2'
    },
    'q3': {
        'alfabeto': 'q2',
        'numeros': 'q4',
        'dot': 'q2',
        'operator': 'q2'
    },
    'q4': {
        'alfabeto': 'q2',
        'numeros': 'q4',
        'dot': 'q2',
        'operator': 'q2'
    }
}

def getSymbol(a):
  if (a in alfabeto):
    return 'alfabeto'
  if (a in numeros):
    return 'numeros'
  if (a in padroes):
    return 'operator'

  return 'dot'

def transition(q, a):
  return automaton[q][a]

def isnumeros(a):
  return a in numeros

def isDot(a):
  return a in dot

def isLastChar(index, size):
  return index == size-1

symbol = ''
state = 'q0'
found = 0

input = '.ab-12.a+12-12-12212.2'

for index, char in enumerate(input):
  symbol = getSymbol(char)
  state = transition(state, symbol)

  if (state == 'q2'):
    state = 'q0'
    found += 1

  if ((state == 'q3') & isLastChar(index, len(input)) & isDot(char)):
    found += 1

  if (isLastChar(index, len(input)) & isnumeros(char)):
    found += 1
    
print(f"A quantidade de padrões é: {found}")