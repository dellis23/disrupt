from __future__ import print_function
import argparse
from itertools import cycle
import os
import platform
from random import randint, choice
import subprocess
from time import sleep


# Text Colors

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
COLORS = (RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN)


# Background Colors

BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_GRAY = '\033[47m'
BG_COLORS = (BG_RED, BG_GREEN, BG_YELLOW, BG_BLUE, BG_MAGENTA, BG_CYAN)


# Cursor Stuff

CURSOR_UP = '\033[1A'
CURSOR_DOWN = '\033[1B'
CURSOR_RIGHT = '\033[1C'
CURSOR_LEFT = '\033[1D'
SAVE_CURSOR = '\033[s'
RESTORE_CURSOR = '\033[u'
HIDE_CURSOR = '\033[?25l'
SHOW_CURSOR = '\033[?25h'
DIRECTIONS = (CURSOR_UP, CURSOR_DOWN, CURSOR_RIGHT, CURSOR_LEFT)


# Misc

CLEAR_SCREEN = '\033[2J'
END = '\033[0m'  # reset colors


def get_interval(verbosity):
    """
    Returns an interval range from 3 at zero verbotiy to 0.01 at verbosity 5.
    """
    return float(-299) / float(500) * verbosity + 3


def random_position(x_size, y_size):
    x, y = randint(1, x_size), randint(1, y_size)
    return "\033[{};{}H".format(x, y)


def get_term():
    return subprocess.check_output(['tty']).strip()


def get_term_size(term):
    # There's gotta be a better way to do this
    flag = '-f' if platform.system() == 'Darwin' else '-F'
    output = subprocess.check_output(['stty', flag, term, 'size'])
    return output.split(' ')


def blocks(term, verbosity):
    """
    Prints a colored box at a random position in the target terminal.
    """
    interval = get_interval(verbosity)
    color_range = (BG_GRAY,) if verbosity <= 2 else BG_COLORS
    dev = os.open(term, os.O_WRONLY)

    while True:
        for color in cycle(color_range):
            term_x, term_y = get_term_size(term)
            move_cursor = random_position(int(term_x), int(term_y))
            os.write(
                dev,
                SAVE_CURSOR + move_cursor + color + ' ' + END + RESTORE_CURSOR
            )
            sleep(interval)


def rainbow(term, verbosity):
    """
    Changes the target terminal's text to a random color.
    """
    interval = get_interval(verbosity)
    dev = os.open(term, os.O_WRONLY)

    while True:
        for color in cycle(COLORS):
            os.write(dev, color)
            sleep(interval)


def jitter(term, verbosity):
    """
    Randomly moves the cursor one movement up, down, left, or right.
    """
    # This is pretty jarring even at the lowest interval, so we double it.
    interval = get_interval(verbosity) * 2
    dev = os.open(term, os.O_WRONLY)

    while True:
        movement = choice(DIRECTIONS)
        os.write(dev, movement)
        sleep(interval)


def wipe(term, verbosity):
    """
    Clears the whole screen.
    """
    # This is pretty jarring even at the lowest interval, so we double it.
    interval = get_interval(verbosity) * 2
    dev = os.open(term, os.O_WRONLY)

    while True:
        os.write(dev, CLEAR_SCREEN)
        sleep(interval)


def hide(term, verbosity):
    """
    Randomly hides or shows the cursor.  Requires the user to type a key for
    it to take effect, so verbosity is basically just maximum.
    """
    interval = 0.01
    dev = os.open(term, os.O_WRONLY)

    while True:
        show_or_hide = choice((SHOW_CURSOR, HIDE_CURSOR))
        os.write(dev, show_or_hide)
        sleep(interval)


def beep(term, verbosity):
    """
    Sends a beep to the target terminal.

    Max verbosity will make them want to kill you, so be courteous.
    """
    # This is one's annoying as hell
    interval = get_interval(verbosity) * 2
    dev = os.open(term, os.O_WRONLY)

    while True:
        os.write(dev, '\a')
        sleep(interval)


def main():

    # Parse Args
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', action='count')
    parser.add_argument('--disruption', '-d', default='blocks')
    parser.add_argument('--terminal', '-t', type=str)
    args = parser.parse_args()
    verbosity = 0 if args.verbose is None else min(5, args.verbose)
    terminal = args.terminal if args.terminal else get_term()

    # Launch Disruption
    disruptions = {
        'rainbow': rainbow,
        'blocks': blocks,
        'jitter': jitter,
        'wipe': wipe,
        'hide': hide,
        'beep': beep,
    }
    assert args.disruption in disruptions, \
        "Disruption {} not found.  Available disruptions: {}".format(
            args.disruption, ", ".join(disruptions))
    disruptions[args.disruption](terminal, verbosity)


if __name__ == '__main__':
    main()
