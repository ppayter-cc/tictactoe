import curses
import curses.textpad
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

win = curses.initscr()
#win = curses.newwin(3, 3, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
#win.border(0)
win.nodelay(1)

curses.noecho()
curses.cbreak()
win.keypad(True)
while True:
    c = win.getch()
    if c == ord('7'):
        win.addstr(0,0,"x")
    elif c == ord('8'):
        win.addstr(0,1,"x")
    elif c == ord('9'):
        win.addstr(0,2,"x")
    elif c == ord('4'):
        win.addstr(1,0,"x")
    elif c == ord('5'):
        win.addstr(1,1,"x")
    elif c == ord('6'):
        win.addstr(1,2,"x")
    elif c == ord('1'):
        win.addstr(2,0,"x")
    elif c == ord('2'):
        win.addstr(2,1,"x")
    elif c == ord('3'):
        win.addstr(2,2,"x")
    elif c == ord('q'):
        break  # Exit the while loop



# mvaddstr() moves to a given y,x coordinate first before displaying the string.
    #form: y, x, str or ch	Move to position y,x within the window, and display str or ch

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
