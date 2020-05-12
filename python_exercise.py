#Object Orient programming in Python
#First we need to create a Class and objects inside of Class
# JOGO Impar and par
from random import randint, choice
nomes = ['petro de Luanda', ' Da gosto', 'Libolo', 'Asa', 'Benfica', 'Inter', 'Kaboscorp',
'Ritondo', 'Kaala', 'Primeiro de Maio', 'Santos', 'Lopes', 'Carlos']
for a in range (1, 4):
    b = choice(nomes)
    print(f' Os times escolhidos sao estes: {b} ')

