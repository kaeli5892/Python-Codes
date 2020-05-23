from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""


def main():
    while front_is_clear():
        put_odd_row()
        put_even_row()

#Karel put beepers on odd number row
def put_odd_row():
    put_checkered_beepers()
    turn_left()
    if front_is_clear():
        move()
        turn_left()

#Karel put beepers on even number row
def put_even_row():
    put_checkered_beepers()
    turn_right()
    if front_is_clear():
        move()
        turn_right()

#Karel put beepers in checkered pattern
def put_checkered_beepers():
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()

#Karel makes a right turn
def turn_right():
    for i in range(3):
        turn_left()


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
