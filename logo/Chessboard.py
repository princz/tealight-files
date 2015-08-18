from tealight.logo import move, turn


   
def row():
  for j in range(0,8):
    square(32)
    move(40)
    
row()
turn(90)
move(60)
row()



