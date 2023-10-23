from classes.board import Board

letter2number = {'A':0, 'B': 1, 'C': 2, 'D':3, 'E': 4, 'F':5, 'G': 6, 'H':7}

board = Board()
 
while True:

    
    start = input("Enter starting coordinates: 'A1-H8' ")
    start = (letter2number[start[0]], int(start[1])-1)
    end = input("Enter ending coordinates: 'A1-H8' ")
    end = (letter2number[end[0]], int(end[1])-1)
    list_coord_pawn = [pawn.coord for pawn in board.list_pawn]
    if start in list_coord_pawn:
        #print('---------------------------')
        index = list_coord_pawn.index(start)
        pawn = board.list_pawn[index]
        list_of_allowed_position = pawn.allowed_move()
        if end in list_coord_pawn:
            print("Not empty")
        else:
            if end in list_of_allowed_position:
                pawn.move(end)
                board.draw()
    

    if input("Continue ? (y/n)") == 'n': break