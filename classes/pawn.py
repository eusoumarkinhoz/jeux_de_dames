class Pawn:
    def __init__(self, color: str, coord: tuple):
        self.color = color
        self.coord = coord
    
    def move(self, new_coord):
        self.coord = new_coord

    def allowed_move(self):
        if self.color == 'Black':
            list_of_allowed_movement = [(-1, 1), (1, 1)]
        elif self.color == 'White':
            list_of_allowed_movement = [(-1, -1), (1, -1)]
        return [(self.coord[0] + direction[0], self.coord[1] + direction[1]) for direction in list_of_allowed_movement]
        