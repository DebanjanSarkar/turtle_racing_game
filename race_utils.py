import turtle

def draw_start__line( start_x_cor: float, screen_height: float ):
    pen = turtle.Turtle()
    pen.pensize(5)
    pen.hideturtle()
    pen.penup()
    pen.setpos( (start_x_cor, screen_height//2 - 50) )
    pen.setheading(270)
    pen.pendown()
    pen.forward( screen_height - 100 )

def draw_finish__line( finish_x_cor: float, screen_height: float ):
    pen = turtle.Turtle()
    pen.pensize(5)
    pen.hideturtle()
    pen.penup()
    pen.setpos( (finish_x_cor, screen_height//2 - 50) )
    pen.setheading(270)
    pen.pendown()
    pen.forward( screen_height - 100 )