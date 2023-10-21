from stanfordkarel import *


def main():
    """Karel code goes here!"""
    move()
    move()
    if no_beepers_present():
        put_beeper()
        move()
    if beepers_present():
        pick_beeper()
    move()
    if no_beepers_present():
        put_beeper()
        move()
    if beepers_present():
        pick_beeper()
    move()
    turn_left()
    turn_left()

    while front_is_clear():
        if beepers_present()
        move()
        move()
        move()
        if beepers_present():
            pick_beeper()





if __name__ == "__main__":
    run_karel_program()
