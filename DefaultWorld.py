from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs.
"""

def main():
    write_joanne()

def write_joanne():
    turn_left()
    move()
    turn_right()
    move()
    letter_h()
    move_2()
    letter_i()
    move_2()
    move()
    letter_j()
    move_2()
    letter_o()
    move_2()
    letter_a()
    move_2()
    letter_n()
    move_2()
    letter_n()
    move_2()
    letter_e()

def move_2():
    move()
    move()

def letter_a():
    paint_corner('blue')
    turn_left()
    for i in range(3):
        paint()
    move()
    turn_right()
    for i in range(3):
        paint()
    move()
    turn_right()
    for i in range(4):
        paint()
    turn_180()
    move()
    move()
    turn_left()
    for i in range(3):
        paint()
    turn_180()
    for i in range(3):
        move()
    turn_right()
    move()
    move()
    turn_left()

def letter_e():
    turn_left()
    paint_corner('blue')
    for i in range(4):
        paint()
    turn_right()
    for i in range(2):
        for i in range(4):
            paint()
        turn_180()
        for i in range(4):
            move()
        turn_left()
        move()
        move()
        turn_left()
    for i in range(4):
        paint()

def letter_h():
    turn_left()
    paint_corner('blue')
    for i in range(4):
        paint()
    turn_right()
    for i in range(4):
        move()
    turn_right()
    paint_corner('blue')
    for i in range(4):
        paint()
    turn_180()
    move()
    move()
    turn_left()
    for i in range(3):
        paint()
    turn_180()
    for i in range(3):
        move()
    turn_right()
    move()
    move()
    turn_left()

def letter_i():
    paint_corner('blue')
    for i in range(4):
        paint()
    turn_180()
    move()
    move()
    turn_right()
    for i in range(4):
        paint()
    turn_right()
    paint()
    paint()
    turn_180()
    move()
    move()
    paint()
    paint()
    turn_left()
    for i in range(4):
        move()
    turn_left()
    for i in range(3):
        move()

def letter_j():
    move()
    turn_left()
    paint()
    turn_180()
    paint()
    turn_left()
    paint()
    paint()
    turn_left()
    for i in range(4):
        paint()
    turn_left()
    paint()
    paint()
    turn_180()
    move()
    move()
    paint()
    paint()
    turn_right()
    for i in range(4):
        move()
    turn_left()

def letter_n():
    turn_left()
    paint_corner('blue')
    for i in range(3):
        paint()
    move()
    turn_right()
    for i in range(3):
        paint()
    move()
    turn_right()
    for i in range(4):
        paint()
    turn_left()

def letter_o():
    paint_corner('blue')
    for i in range(4):
        paint()
    turn_left()
    for i in range(4):
        paint()
    turn_left()
    for i in range(4):
        paint()
    turn_left()
    for i in range(3):
        paint()
    move()
    turn_left()
    for i in range(4):
        move()

def paint():
    move()
    paint_corner('blue')

def turn_180():
    turn_left()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
