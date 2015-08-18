from tealight.logo import move, turn

def square(side):
  for i in range(0,4):
    move(side)
    turn(90)
   
def row():
  for j in range(0,8):
    square(32)
    move(32)
    
row()
turn(90)
move(64)
turn(90)
row()



