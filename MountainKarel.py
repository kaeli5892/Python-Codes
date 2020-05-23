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

    #MOUNTAIN KAREL SOLUTION

    move_to_mountain()
    climb()
    put_beeper()
    descend()

def move_to_mountain():
    while front_is_clear():
        move()

def climb():
    while front_is_blocked():
        turn_left()
        move()
        turn_right()
        move()

def descend():
    while front_is_clear():
        move()
        turn_right()
        if front_is_clear():
            move()
            turn_left()
        else:
            turn_left()


def turn_right():
    for _ in range(3):
        turn_left()

    #MOUNTAIN KAREL END

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
