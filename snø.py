import sys
import os
import time
import random
import math

stack = []
code = []
char = ''

# Search for file arguments

if len(sys.argv) == 1:
  file_argument = 'main.sn'
else:
  file_argument = sys.argv[1]

# Open the file

with open(file_argument, 'r') as file:
    for line in file:
        row = [char if char != ' ' else ' ' for char in line.rstrip('\n')]
        code.append(row)

code = [row + [''] * (max(len(row) for row in code) - len(row)) for row in code]

x = 0
y = 0
direction = 'init'

directions = ['bl', 'br']
numbers = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def run():
  global stack, char, code, x, y, direction, numbers

  # Update direction & current command

  while y < len(code) and x < len(code[y]):

    if direction == 'bl':
      x -= 1
      y += 1
    
    elif direction == 'br':
      x += 1
      y += 1

    elif direction == 'init':
      x += 1
    
    char = code[y][x] if y < len(code) and x < len(code[y]) else ''
    ### print('\033[30m' + char); print('\033[31m' + direction); print('\033[0m', end = '')

    # Direction commands

    if char == '/':
      direction = 'bl'
    
    elif char == '\\':
      direction = 'br'

    elif char == '§':
      direction = directions[random.randint(0,1)]

    elif char == '&':
      sys.exit()

    # IO commands

    elif char == 'I':
      stack.append(chr(input().encode('utf-8')[0]))
    
    elif char == 'O':
      print(stack.pop(), end='')

    # Stack manipulation commands

    elif char == '!':
      stack.pop()
    
    elif char in numbers:
      stack.append(int(char, 16))

    elif char == ':':
      stack.append(stack[-1])

    elif char == '}':
      stack[-1], stack[-2] = stack[-2], stack[-1]

    elif char == '$':
      stack.reverse()

    # Math commands

    elif char == '+':
      stack.append(int(stack.pop()) + int(stack.pop()))

    elif char == '-':
      a = int(stack.pop())
      b = int(stack.pop())
      stack.append(b - a)

    elif char == '*':
      stack.append(int(stack.pop()) * int(stack.pop()))

    elif char == '|':
      a = stack.pop()
      b = stack.pop()
      stack.append(b / a)

    elif char == '%':
      a = int(stack.pop())
      b = int(stack.pop())
      stack.append(a % b)

    elif char == '^':
      a = int(stack.pop())
      b = int(stack.pop())
      stack.append(b ** a)

    elif char == '~':
      a = int(stack.pop())
      b = int(stack.pop())
      stack.append(~(b | a))

    # Misc

    elif char in ('Y', '¥', 'λ', '⅄'):
      if int(stack.pop()) != 0:
        direction = 'bl'
      else:
        direction = 'br'

    elif char == '@':
      x = x
      y = y
      direction = 'bl'

    elif not any('@' == value for row in code for value in row):
      sys.stderr.write('\n\n\033[31mNo `@` found in the code')
      sys.exit()

    
      

try:
  run()
except KeyboardInterrupt:
  sys.stderr.write('\n\n\033[31mExited with ^C')
except IndexError: 
  sys.stderr.write('\n\n\033[31mStack underflow')