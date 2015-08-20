from tealight.art import (line, spot, circle, box, rectangle, image, text, background, color)

grid = []
for row in range(64):
  grid(row).append([])
     
for column in range(10):
  grid(row).append([])
  
print grid