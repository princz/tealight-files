from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

def run(i):
  for i in range(0,3):
    move()
    
    
def run1(i):
  for i in range(0,20):
    move()
        
    
run(0)
turn(1)
run1(0)
turn(1)

