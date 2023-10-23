from classes.pawn import Pawn

pawns = []
for y in range (0,8):
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
