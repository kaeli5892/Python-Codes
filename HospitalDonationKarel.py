from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
During the COVID pandemic, hospital is desperately in need of supply.
Karel is going to each hospital in his world and put a beeper into the
donation box!
"""

def main():
    while front_is_clear():
        donate_to_hospital()


def donate_to_hospital():
    while front_is_clear():
        move()
        turn_left()
        if front_is_blocked():
            turn_right()
            for a in range(3):
                move()
            put_beeper_in_box()
            leave_hospital()
        else:
            turn_right()

def put_beeper_in_box():
    turn_left()
    move()
    move()
    turn_left()
    move()
    turn_left()
    move()
    put_beeper()

def leave_hospital():
    turn_around()
    move()
    turn_right()
    move()
    turn_right()
    move()
    move()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    for a in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
