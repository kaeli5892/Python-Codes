from karel.stanfordkarel import *

# File: hospital.py
# -----------------------------
# Here is a place to program your section problem
def main():

#Build Hospital code

   while front_is_clear():
      if beepers_present():
         build_hospital()
         if front_is_clear():
            move()
      else:
         move()

def place_two_beepers():
       for i in range(2):
          move()
          put_beeper()

def build_hospital():
   turn_left()
   place_two_beepers()

   #turn around
   turn_right()
   move()
   turn_right()
   place_two_beepers()
   put_beeper()
   turn_left()


def turn_right():
   for i in range(3):
      turn_left()


   # add your code here
