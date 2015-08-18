from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
def run(i):
  while i < 16:
    move()
    i + 1
  turn(1)
  
run(0)