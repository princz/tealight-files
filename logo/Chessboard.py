from tealight.logo import move, turn

def square(side):
  for i in range(0,4):
    move(side)
    turn(90)

for i in range(0,8):
    turn(90)

