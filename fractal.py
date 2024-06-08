"""Module providing a function drawing koch snowflake ."""
import turtle

def koch_curve(t, order, size):
    """Function creating koch curve"""
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_curve(t, order-1, size)
        t.left(60)
        koch_curve(t, order-1, size)
        t.right(120)
        koch_curve(t, order-1, size)
        t.left(60)
        koch_curve(t, order-1, size)

def koch_snowflake(t, order, size):
    """Function creating koch snowflake"""
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def main():
    """Function drawing koch snowflake"""
    order = int(input("Enter the recursion level: "))
    size = 300

    turtle.speed(0)
    t = turtle.Turtle()
    t.penup()
    t.goto(-size/2, size/3)
    t.pendown()

    koch_snowflake(t, order, size)
    turtle.done()

if __name__ == "__main__":
    main()
