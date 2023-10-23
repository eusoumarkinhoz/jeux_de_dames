print("yyyyyozhfzoe")

import curses

class CheckersGame:
    def __init__(self, stdscr):
        curses.curs_set(0)  # Hide cursor
        self.stdscr = stdscr
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.current_player = 1  # Player 1 starts


def print_board(self):
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece == 0:
                    self.stdscr.addstr(i * 2, j * 4, "    ")
                elif piece == 1:
                    self.stdscr.addstr(i * 2, j * 4, " 1  ", curses.color_pair(1))
                elif piece == 2:
                    self.stdscr.addstr(i * 2, j * 4, " 2  ", curses.color_pair(2))
                elif piece == 3:
                    self.stdscr.addstr(i * 2, j * 4, " 1K ", curses.color_pair(1))
                elif piece == 4:
                    self.stdscr.addstr(i * 2, j * 4, " 2K ", curses.color_pair(2))
            self.stdscr.addstr(i * 2 + 1, 0, "-" * 32)

        self.stdscr.refresh()
def handle_input(self):
        key = self.stdscr.getch()
        if key == ord('q'):
            return False  # Exit the game if 'q' is pressed
        return True

    def play(self):
        while True:
            self.stdscr.clear()  # Clear the screen
            self.print_board()
            if not self.handle_input():
                break

if __name__ == "__main__":
    curses.wrapper(lambda stdscr: CheckersGame(stdscr).play())