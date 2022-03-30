import random
import turtle
skk = turtle.Turtle()
 
for i in range(100):
    skk.forward(random.randint(10,50))
    skk.right(random.randint(10,1000))
     
turtle.done()
