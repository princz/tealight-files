from random import random
r=16
c=16
HighestNoMines = 10.0

Nc=0
while (Nc == 0):
  Nc=int(random()*HighestNoMines)

p=Nc/(r*c)

print p
  
#for i in range(0,Nc):
m=[]
for j in range(0,r-1):
  m.append([])
  for k in range(0,c-1):
    
    m[j].append(0)
    
print m
