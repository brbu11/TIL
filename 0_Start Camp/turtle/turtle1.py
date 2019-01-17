import turtle as t 

class MagicBrush:
    t.color('red')
    def draw_triangle(self):
        for i in range(3):
            t.forward(100)
            t.right(120)
    def draw_square(self):
        for i in range(4):
            t.forward(100)
            t.right(90)
    def go(self):
        t.forward(250)
    def turn(self):
        t.right(180)

# m1 = MagicBrush()
# m2 = MagicBrush()
brad = t.Turtle()
brad.shape("turtle")
brad.speed(2)
brad.forward(200)
# m1.draw_square()
# m2.go()

# m1.draw_triangle()
# m2.draw_triangle()
# m1.turn()
# m2.turn()
# m1.draw_square

t.mainloop()
