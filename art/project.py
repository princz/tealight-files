from random import random
r=16
c=16
HighestNoMines = 10

Nc=0
while (Nc == 0):
  Nc=int(random()*HighestNoMines)

#for i in range(0,Nc):

for j in range(0,r-1):
  for k in range(0,c-1):
    m[r][c]=0
    
print m
