import time
import turtle
print("welcome to the star bank, we draw stars")
time.sleep(2.5)
print("i only can do red and yellow, but those are pretty nice, don't you think?")
time.sleep(3)
print("anyway, you gotta choose either red or yellow. \n*please don't capitalize anything*")
a = input("I want the star to be...")
if a == "red":
  from turtle import* 
  color('red')
  counter = 0
  while counter <=  4: 
    turtle.right(72) 
    turtle.forward(100)
    turtle.right(72)
    counter += 1
if a == "yellow":
  from turtle import*
  color('yellow')
  counter = 0
  while counter <=  4: 
    turtle.right(72) 
    turtle.forward(100)
    turtle.right(72)
    counter += 1
print("hope you like it :)")
