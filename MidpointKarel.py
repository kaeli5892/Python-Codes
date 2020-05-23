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
    '''
#MOUNTAIN KAREL SOLUTION

    while front_is_clear():
        move()
    turn_left()

#MOUNTAIN KAREL END

    '''

#MIDPOINT KAREL SOLUTION

    move_to_end()
    turn_left()
    move_to_end()
    turn_180()
    while front_is_clear():
        step()
    put_beeper()


def move_to_end():
    #Karel is going to move from the corner to the next corner
    while front_is_clear():
        move()

def step():
    #Karel is going to move down two steps
    if front_is_clear():
        move()
        #This is to prevent Karel from crashing if he can only moves down 1 step
        if front_is_clear():
            move()
        else:
            #Karel is going left 1 step
            turn_left()
            if front_is_clear():
                move()
                turn_right()
    turn_right()
    #Karel is going left 1 step
    if front_is_clear():
        move()
    turn_left()

def turn_180():
    #Karel is going to turn around 180 degrees
    turn_left()
    turn_left()

def turn_right():
    #Karel is going to make a right turn
    for i in range(3):
        turn_left()


#     count = 0
#     while front_is_clear():
#         move()
#         count = count + 1
#     steps = int(count%2 + int(count/2))
#     turn_180()
#     for step in range(steps):
#         if front_is_clear():
#             move()
#     put_beeper()
#
# def turn_180():
#     turn_left()
#     turn_left()

#MIDPOINT KAREL END


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
