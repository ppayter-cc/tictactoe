import curses
import curses.textpad
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint



screen = curses.initscr()
#bo = curses.initscr()
dims = screen.getmaxyx()
screen = curses.newwin(int(dims[0]), int(dims[1]),0 ,0)
screen.box()
for i in range (0, int(dims[0])):
    screen.addstr(i, int(dims[1]/3), '|')
    screen.addstr(i, int(dims[1]/3*2), '|')
for i in range (0, int(dims[1])):
    screen.addstr(int(dims[0]/3), i, '_')
    screen.addstr(int(dims[0]/3*2), i, '_')
    #screen.addstr(i, int(dims[1]), '|')
    #screen = curses.newwin(int(dims[0]/3),int(dims[1]/3),int(dims[0]-dims[0]/3) ,int(dims[1]-dims[1]/3))

curses.noecho()
curses.cbreak()
screen.keypad(True)

while True:
    c = screen.getch()
    if c == ord('7'):
        screen.addstr(0,0,"x")
    elif c == ord('8'):
        screen.addstr(0,1,"x")
    elif c == ord('9'):
        screen.addstr(0,2,"x")
    elif c == ord('4'):
        screen.addstr(1,0,"x")
    elif c == ord('5'):
        screen.addstr(1,1,"x")
    elif c == ord('6'):
        screen.addstr(1,2,"x")
    elif c == ord('1'):
        screen.addstr(2,0,"x")
    elif c == ord('2'):
        screen.addstr(2,1,"x")
    elif c == ord('3'):
        screen.addstr(2,2,"x")
    elif c == ord('q'):
        break  # Exit the while loop



# mvaddstr() moves to a given y,x coordinate first before displaying the string.
    #form: y, x, str or ch	Move to position y,x within the window, and display str or ch

curses.nocbreak()
screen.keypad(False)
curses.echo()
curses.endwin()
