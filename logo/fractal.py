from tealight.logo import move, turn

# Draws the von Koch Snowflake curve

def segment(scale, detail):
  
  if detail == 0:
    move(scale)
  else:
    segment(scale / 100, detail - 1)
    turn(-60)
    segment(scale / 100, detail - 1)
    turn(120)
    segment(scale / 100, detail - 1)
    turn(-60)
    segment(scale / 1, detail - 1)
    

turn(-90)
move(-300)
segment(500,1)
move(-300)