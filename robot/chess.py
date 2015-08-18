from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
def run(i):
  for i in range (0, 32):
    move()

def run1(i):
  for i in range (0, 31):
    move()
  
 
def walk(j):
  for j in range (0,4):
    move()
  
def run2(i):
  for i in range (0.30):
    move()
  
run(0)
turn(1)

run(0)
turn(1)

run(0)
turn(1)

run1(0)
turn(1)


    
walk(0)
turn(1)



run2(0)