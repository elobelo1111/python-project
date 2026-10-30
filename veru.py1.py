import turtle 
screen=turtle.Screen()
t=turtle.Turtle()

def draw_shape(n,size):
    for _ in range(n):
        t.forward(size)
        t.left(360/n)

t.speed(5)
t.fillcolor("purple")
t.begin_fill()
draw_shape(3,100)
t.setx(120)
t.end_fill()

t.fillcolor("orange")
t.begin_fill()
draw_shape(3,100)
t.setx(-240)
t.end_fill()

t.fillcolor("purple")
t.begin_fill()
draw_shape(3,100)
t.setx(-120)
t.end_fill()

t.fillcolor("orange")
t.begin_fill()
draw_shape(3,100)
t.end_fill()































# draw_shape(6,100)


# t.pencolor("red")
# t.speed(15)
# for _ in range(36):
#     t.left(10)
#     for _ in range(5):
#         t.forward(100)
#         t.left(144)
# shape=screen.textinput("shape","enter the shape name")    
# color=screen.textinput("color","enter the color name")  
# t.fillcolor(color)
# t.begin_fill()
# if shape=="square":
#     draw_shape(4,100)
# elif shape=="triangle":
#     draw_shape(3,100)    
# elif shape=="circle":
#     t.circle(100)
# else:
#     print("invalid shape name")
    
# t.end_fill()

turtle.done()