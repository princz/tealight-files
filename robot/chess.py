from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here


def run(i):
  for i in range (0,4):
    move()
    turn(1)
    
run(4)

