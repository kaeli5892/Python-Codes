from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""


def main():
    #Karel is preparing to go up to the top of a column
    for i in range(3):
        turn_left()
        #going up and reparing the column
        up()
        #going down
        down()
        #rinse and repeat
        turn_left()
        move_4()
    turn_left()
    up()

def up():
    #Karel is going up to the top of a column
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()
    if no_beepers_present():
        put_beeper()

def down():
    #Karel is going down to the bottom of a column
    turn_180()
    while front_is_clear():
        move()

def turn_180():
    #Karel is going to turn around 180 degrees
    turn_left()
    turn_left()

def move_4():
    #Karel is going to take four steps
    for i in range(4):
        move()

def turn_right():
    #Karel is turning right by turning left 3x
    for i in range(3):
        turn_left()

"""
    turn_left()
    for i in range(2):
        put_beeper()
        move()
    put_beeper()
    turn_right()
    move_4_steps()
    put_beeper()
    turn_left()
    move()
    move()
    put_beeper()
    turn_right()
    move_4_steps()
    turn_right()
    move()
    put_beeper()
    move()
    for i in range(2):
        move()
        put_beeper()
    turn_left()
    move_4_steps()
    turn_left()
    for i in range(2):
        move()
        put_beeper()
        move()

def move_4_steps():
    for i in range(4):
        move()

def turn_right():
    for i in range(3):
        turn_left()
"""
"""
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
"""
#    pass


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
