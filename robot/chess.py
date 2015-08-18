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


  
run(0)
turn(1)

run(0)
turn(1)

run(0)
turn(1)

jog(0)
turn(1)

def walk(j):
  for j in range (0,4):
    move()
    
walk(0)
turn(1)

def jog(i):
  for i in range (0, 31):
    move()

jog(0)