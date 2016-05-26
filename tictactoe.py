import curses
import curses.textpad


board = [' '] * 10

playernames = [input("Enter name for player 'X': "), input("Enter name for player 'O': ")]


z = 0  # for the 'test' function


def current_player():
    global z
    if z == 0:
        return screen.addstr(5, 1, playernames[0] + " is next!" + " "*30)
    elif z == 1:
        return screen.addstr(5, 1, playernames[1] + " is next!" + " "*30)


def test(i):  # alternates between 'X' and 'O'
    global z
    if z == 0:
        z += 1
        s = 'X'
        board[i] = s  # fills the list of moves with the players' symbols
        return "X"
    else:
        s = "O"
        board[i] = s
        z -= 1
        return "O"


def rewrite(i):  # to avoid overwriting existing steps
    global board
    global write
    global c
    if board[i] == " ":
        write = True
    else:
        write = False


def get_player_move(c):  # prints the players' symbols on the space associated with the num keys
    if c == ord('7'):
        i = 7
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/8*3), int(dims[1]/6), test(i))
    elif c == ord('8'):
        i = 8
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/8*3), int(dims[1]/2), test(i))
    elif c == ord('9'):
        i = 9
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/8*3), int(dims[1]/6*5), test(i))
    elif c == ord('4'):
        i = 4
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/8*5), int(dims[1]/6), test(i))
    elif c == ord('5'):
        i = 5
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/8*5), int(dims[1]/2), test(i))
    elif c == ord('6'):
        i = 6
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/8*5), int(dims[1]/6*5), test(i))
    elif c == ord('1'):
        i = 1
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/8*7), int(dims[1]/6), test(i))
    elif c == ord('2'):
        i = 2
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/8*7), int(dims[1]/2), test(i))
    elif c == ord('3'):
        i = 3
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/8*7), int(dims[1]/6*5), test(i))
    return()


def winner1():  # returns true if player1 wins
    ply1 = "X"
    global board
    return ((board[7] == ply1 and board[8] == ply1 and board[9] == ply1) or  # horizontal
            (board[4] == ply1 and board[5] == ply1 and board[6] == ply1) or  # horizontal
            (board[1] == ply1 and board[2] == ply1 and board[3] == ply1) or  # horizontal
            (board[7] == ply1 and board[4] == ply1 and board[1] == ply1) or  # vertical
            (board[8] == ply1 and board[5] == ply1 and board[2] == ply1) or  # vertical
            (board[9] == ply1 and board[6] == ply1 and board[3] == ply1) or  # vertical
            (board[7] == ply1 and board[5] == ply1 and board[3] == ply1) or  # diagonal
            (board[9] == ply1 and board[5] == ply1 and board[1] == ply1))  # diagonal


def winner2():  # returns true if player2 wins
    ply2 = "O"
    global board
    return ((board[7] == ply2 and board[8] == ply2 and board[9] == ply2) or  # horizontal
            (board[4] == ply2 and board[5] == ply2 and board[6] == ply2) or  # horizontal
            (board[1] == ply2 and board[2] == ply2 and board[3] == ply2) or  # horizontal
            (board[7] == ply2 and board[4] == ply2 and board[1] == ply2) or  # vertical
            (board[8] == ply2 and board[5] == ply2 and board[2] == ply2) or  # vertical
            (board[9] == ply2 and board[6] == ply2 and board[3] == ply2) or  # vertical
            (board[7] == ply2 and board[5] == ply2 and board[3] == ply2) or  # diagonal
            (board[9] == ply2 and board[5] == ply2 and board[1] == ply2))  # diagonal


def winning():  # whether one of the players won, prints this text
    if winner1():
        screen.addstr(5, 1, "♛  " + playernames[0] + " won! ♛" + " "*30)
    elif winner2():
        screen.addstr(5, 1, "♛  " + playernames[1] + " won! ♛" + " "*30)
    return()


screen = curses.initscr()  # draws the board
dims = screen.getmaxyx()
screen = curses.newwin(int(dims[0]), int(dims[1]), 0, 0)
screen.box()
for i in range(int(dims[0]/4), int(dims[0])):
    screen.addstr(i, int(dims[1]/3), '|')  # vertical
    screen.addstr(i, int(dims[1]/3*2), '|')
for i in range(0, int(dims[1])):
    screen.addstr(int(dims[0]/4), i, '_')
    screen.addstr(int(dims[0]/2), i, '_')  # horizontal
    screen.addstr(int(dims[0]/4*3), i, '_')
screen.addstr(1, 1, "►► ► TIC-TAC-TOE ◄ ◄◄")
screen.addstr(2, 1, "Use number keys to place 'X' and 'O'.")
screen.addstr(3, 1, "Press 'q' to quit or press 'r' to restart.")
screen.addstr(5, 1, playernames[0] + " is next!" + " "*30)


curses.noecho()
curses.cbreak()
screen.keypad(True)
curses.curs_set(0)

while True:
    if winner1() or winner2():  # if one of the players won
        winning()
        board = ['-'] * 10  # fills the board list to prevent more moves
        z = 5

    c = screen.getch()

    if c == ord('q'):  # if 'q' pressed the game exits
        break  # Exit the while loop
    elif c == ord('r'):
        screen = curses.initscr()  # draws the board
        dims = screen.getmaxyx()
        screen = curses.newwin(int(dims[0]), int(dims[1]), 0, 0)
        screen.box()
        for i in range(int(dims[0]/4), int(dims[0])):
            screen.addstr(i, int(dims[1]/3), '|')  # vertical
            screen.addstr(i, int(dims[1]/3*2), '|')
        for i in range(0, int(dims[1])):
            screen.addstr(int(dims[0]/4), i, '_')
            screen.addstr(int(dims[0]/2), i, '_')  # horizontal
            screen.addstr(int(dims[0]/8*6), i, '_')
        screen.addstr(1, 1, "►► ► TIC-TAC-TOE ◄ ◄◄")
        screen.addstr(2, 1, "Use number keys to place 'X' and 'O'.")
        screen.addstr(3, 1, "Press 'q' to quit or press 'r' to restart.")
        screen.addstr(5, 1, playernames[0] + " is next!" + " "*30)
        board = [' '] * 10
        z = 0
    elif c != ord('q'):  # if 'q' is not pressed the game continues
        get_player_move(c)
        current_player()


curses.nocbreak()
screen.keypad(False)
curses.echo()
curses.endwin()
