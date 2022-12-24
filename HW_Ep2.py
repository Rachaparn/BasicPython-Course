import turtle
color = ['red','purple','blue','green']
tao = turtle.Pen()
tao.speed(0)
turtle.bgcolor('grey')
def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()
    print(x)
    print(y)


def Draw():
    for i in range(90):
        tao.pencolor(color[i%4])
        tao.width(i/70+1)
        tao.circle(i)
        tao.left(59)


Go(200,100)
Draw()
Go(-400,100)
Draw()
Go(-50,-200)
Draw()








