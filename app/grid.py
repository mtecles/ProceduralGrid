import math
from settings import *


class Grid(object):
    """ Represent the grid that contains rooms and cells """

    def __init__(self):
        self.layout_file = None
        self.rooms = []
        self.w = SIZE['LAYOUT']['W']
        self.h = SIZE['LAYOUT']['H']
        self.columns_nb = math.floor(self.w / SIZE['CELL']['W'])
        self.lines_nb = math.floor(self.h / SIZE['CELL']['H'])

    @property
    def size(self):
        return (self.w, self.h)

    @property
    def cells_nb(self):
        return self.columns_nb * self.lines_nb

    @property
    def rooms_nb(self):
        return len(self.rooms)

    def add_room(self, cells):
        assert (int(cells) >= SIZE['MIN_ROOM_CELLS'])
        assert (int(cells) <= SIZE['MAX_ROOM_CELLS'])
        room = Room(self.rooms_nb, cells)
        self.rooms.append(room)
        return room

    def get_room(self, room_id):
        for room in self.rooms:
            if room_id == room.id:
                return room


class Room(object):
    """ Represent a room that contains cells """

    def __init__(self, index, cells):
        self.id = index
        self.cells = []
        for c in range(0, cells):
            self.cells.append(Cell(self.cells_nb))

    @property
    def cells_nb(self):
        return len(self.cells)

    def get_cell(self, cell_id):
        for cell in self.cells:
            if cell_id == cell.id:
                return cell


class Cell(object):
    """ Represent an unique cell """

    def __init__(self, index):
        self.id = index
