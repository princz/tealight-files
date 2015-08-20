from random import random
#from github.jackm110.art.Project import *

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

