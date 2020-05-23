from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the
Triple sample worlds supplied in the starter folder.
"""


def main():
    paint_3_buildings()

def paint_3_buildings():
    #paint the 2 west walls
    for a in range(2):
        for i in range(2):
            paint_wall()
            next_wall()
        #paint the south wall
        paint_wall()
        turn_right()

    for i in range(2):
        #more wall painting
        paint_wall()
        next_wall()

    #for i in range(2):
        #paint the inner walls
        #paint_wall()
        #turn_right()

    paint_wall()

def paint_wall():
    #this is a function to paint wall if Karel detect a wall
    while left_is_blocked():
        put_beeper()
        move()

def turn_right():
    #turn right by turning left 3x
    for i in range(3):
        turn_left()

def next_wall():
    #Karel will keep moving until he finds next wall
    turn_left()
    move()

"""
    paint_reg()
    turn_180()
    for i in range(4):
        move()
    turn_left()
    move()
    turn_right()
    paint_small_reg()
    turn_180()
    for i in range(4):
        move()
    turn_right()
    paint_square()

def paint_square():
    for i in range(4):
        paint_short()
        turn_left()
        move()

def paint_small_reg():
    for i in range(2):
        move()
        put_beeper()
    move()
    turn_right()
    move()
    paint_short()
    turn_right()
    for i in range(2):
        move()
        put_beeper()
    move()
    turn_right()
    move()
    paint_short()

def paint_long():
    for i in range(4):
        put_beeper()
        move()

def paint_short():
    for i in range(3):
        put_beeper()
        move()

def paint_reg():
    for i in range(2):
        paint_long()
        turn_left()
        move()
        paint_short()
        turn_left()
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_180():
    turn_left()
    turn_left()

"""

"""
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
"""
    #pass


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
