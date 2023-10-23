class Move:
    pawn_color = str(input("Enter color: "))
    start_row = int(input("Enter starting row: ")
    start_col = int(input("Enter starting column: ")
    end_row = int(input("Enter ending row: ")
    end_col = int(input("Enter ending column: ")
    if Pawn(color = pawn_color, coord = (start_row,start_col)):
        Pawn(color = pawn_color, coord = (end_row,end_col))