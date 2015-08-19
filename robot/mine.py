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
        
    
while True: 
  move()
  if touch()=='wall':
    if left_side()==None:
      turn(-1)
    elif right_side()==None:
      turn(1)
    elif touch()=='wall':
       turn(-1)
    else:
      turn(2)
  
  elif left_side()==None:
    turn(-1)

