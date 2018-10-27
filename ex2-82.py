import turtle as t
t.pensize(3)
t.color("green")
t.width(3)
t.seth(90)
t.speed(15)
for i in range(100):
    t.fd(5*i)
    t.seth(90+90*i)
t.done()
