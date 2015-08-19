from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import sin, cos, pi

def elipses(x, y, c, size, size2):
  
  color(c)
  
  angle = 0
  
  for i in range(0,size2):
    x0 = x + (size * cos(angle))
    y0 = y + (size * sin(angle))
    
    line(x, y, x0, y0)
    
    angle = angle + (2 * pi / size2)

elipses(350, 400, "blue", 100,999)
elipses(400, 400, "purple", 100,999)
elipses(450, 400, "orange", 100,999)