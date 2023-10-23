from .pawn import Pawn

class Board:

    def __init__(self):
        #List of pawns
        pawns = []
        for y in range (0, 8):
            if (y%2 == 0) and (y < 3):
                for x in range(1, 8, 2):
                    a_pawn = (x,y)
                    #print(a_pawn)
                    pawns.append(Pawn(color = 'Black', coord = a_pawn))
            elif (y%2 != 0) and (y < 3):
                for x in range(0, 8, 2):
                    a_pawn = (x,y)
                    #print(a_pawn)
                    pawns.append(Pawn(color = 'Black', coord = a_pawn))
            if (y%2 == 0) and (y > 4):
                for x in range(1, 8, 2):
                    a_pawn = (x,y)
                    #print(a_pawn)
                    pawns.append(Pawn(color = 'White', coord = a_pawn))
            elif (y%2 != 0) and (y > 4):
                for x in range(0, 8, 2):
                    a_pawn = (x,y)
                    #print(a_pawn)
                    pawns.append(Pawn(color = 'White', coord = a_pawn))    
            y += 1
        
        self.list_pawn = pawns
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


