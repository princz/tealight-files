from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import sin, cos, pi

def elipses(x, y, c, size):
  
  color(c)
  
  angle = 0
  
  for i in range(0,1):
    x0 = x + (size * cos(angle))
    y0 = y + (size * sin(angle))
    
    line(x, y, x0, y0)
    
    angle = angle + (2 * pi / 1)

star(350, 400, "blue", 10, 999)
star(400, 400, "purple", 10, 999)
star(450, 400, "orange", 10, 999)