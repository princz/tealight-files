from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
def run(i):
  while i < 10:
    move()
    i + 1

  
run(0)
turn(1)