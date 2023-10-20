from .pawn import Pawn

class Board:
    def __init__(self):
        self.list_pawn = [
            Pawn(color = 'Black', coord = (3,3)),
            Pawn(color = 'Black', coord = (4,4)),
            Pawn(color = 'White', coord = (4,3)),
            Pawn(color = 'White', coord = (3,4)),

            ]
        self.draw()

    def draw(self):
        # Print board vide
        msg = list(('+---'*8 + '+\n' + '|   '*8 + '|\n')*8 + '+---'*8 + '+\n')

        for pawn in self.list_pawn:

            index = (34 + pawn.coord[0]*4) + 2*(34*pawn.coord[1]+1)
            if pawn.color == "White":
                msg[index] = 'O'
            elif pawn.color == "Black":
                msg[index] = 'X'

        msg = ''.join(a for a in msg)
        print(msg)


