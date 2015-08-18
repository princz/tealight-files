from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
while True: 
  move()
  if touch()=='wall':
    if left_side()==None:
      turn(-1)
    elif right_side()==None:
      turn(1)
    else:
      turn(2)
  if left_side()==None:
    turn(-1)
  
 