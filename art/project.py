from random import random
r=16
c=16
HighestNoMines = 10

Nc=0
while (Nc == 0):
  Nc=int(random()*HighestNoMines)

p=float(Nc)/float(r*c)

def check(x,y):

  count = 0 

  if m[x-1][y-1] == 1:
    count=count+1
  if m[x][y-1] == 1:  
    count=count+1
  if m[x+1][y-1] == 1:    
    count=count+1
  if m[x+1][y] == 1:    
    count=count+1
  if m[x+1][y+1] == 1:    
    count=count+1  
  if m[x][y+1] == 1:    
    count=count+1
  if m[x-1][y+1] == 1:    
    count=count+1
  if m[x-1][y] == 1:    
    count=count+1
    
  return count
  
#for i in range(0,Nc):
m=[]
for j in range(0,r-1):
  m.append([])
  for k in range(0,c-1):
    mine=random()
    if (mine <= p):
      m[j].append(1)
    else:
      m[j].append(0)

m[0][1]=1

print check(1,1)
print m


