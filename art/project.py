from random import random
r=16
c=16
HighestNoMines = 10

Nc=0
while (Nc == 0):
  Nc=int(random()*HighestNoMines)

for i in range(0,Nc):
  print i