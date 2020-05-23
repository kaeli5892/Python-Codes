from karel.stanfordkarel import *

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""



def main():
    clean_up()
    turn_left()
    while front_is_clear():
        next_row()
        #move to the start of the row
        move_forward()
        turn_180()
        #start the clean up
        clean_up()
        turn_left()


def turn_180():
    turn_left()
    turn_left()

def next_row():
    move()
    turn_left()

def move_forward():
    while front_is_clear():
        move()

def clean_up():
    if beepers_present():
        pick_beeper()
    while front_is_clear():
        move()
        if beepers_present():
            pick_beeper()

"""
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
"""
    # pass


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
