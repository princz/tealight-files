from random import random
import github.jackm110.art.Project.py

r=16
c=16
HighestNoMines = 30

Nc=0
while (Nc == 0):
  Nc=int(random()*HighestNoMines)

p=float(Nc)/float(r*c)

def isMine(x,y):
  if x < 0 or x > 16:
    return 0
  if y < 0 or y > 16:
    return 0
  return m[x][y]

def check(x,y):

  count = 0 

  if isMine(x-1, y-1) == 1:
    count=count+1
  if isMine(x, y-1) == 1:  
    count=count+1
  if isMine(x+1, y-1) == 1:    
    count=count+1
  if isMine(x+1, y) == 1:    
    count=count+1
  if isMine(x+1, y+1) == 1:    
    count=count+1  
  if isMine(x, y+1) == 1:    
    count=count+1
  if isMine(x-1, y+1) == 1:    
    count=count+1
  if isMine(x-1, y) == 1:    
    count=count+1
    
  return count

flags=[]

def initial():
  for j in range(0, r-1):
    flags.append([])
    for k in range(0, c-1):
      flags.append(0)

def flag(x,y):
  flags[x][y] = 1
  
def clear(x,y):
  flags[x][y] = 2
  
  
  
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

print check(0,2)
print m
initial()