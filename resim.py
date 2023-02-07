import turtle
import sys,time

t = turtle.Turtle()
t.shape("turtle")
t.color("black","black")

#1.proje başlangıç
t.forward(100)
t.left(90)
time.sleep(0.10)
t.up()
t.forward(100)
t.left(90)
t.down()
t.forward(100)
time.sleep(1)
#bitiş

t.up()
t.forward(100)
t.down()

#2.proje başlangıç
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(180)
time.sleep(3)
#bitiş

t.up()
t.forward(200)
t.left(90)
t.down()

#3.proje başlangıc
t.color("red","red")
t.forward(50)
t.up()
t.forward(50)
t.down()

t.color("yellow","yellow")
t.forward(50)
t.up()
t.forward(50)
t.down()

t.color("blue","blue")
t.forward(50)
time.sleep(3)
#bitiş

t.up()
t.goto(-130,-190)
t.down()
t.up()
t.write("Ali Behram Albayrak", font=("Verdana", 17,"bold"))
t.goto(130,190)
time.sleep(10)
