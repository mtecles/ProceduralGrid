# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
from settings import *
from app.grid import Grid


class GridTest(unittest.TestCase):

    def setUp(self):
        self.grid = Grid()

    def test_no_grid_file(self):
        self.assertIsNone(self.grid.layout_file)

    def test_grid_default_size(self):
        self.assertEqual(self.grid.w, SIZE['LAYOUT']['W'])
        self.assertEqual(self.grid.h, SIZE['LAYOUT']['H'])
        self.assertEqual(self.grid.size, (SIZE['LAYOUT']['W'], SIZE['LAYOUT']['H']))

    def test_columns_and_lines_number(self):
        self.assertEqual(self.grid.columns_nb, 10)
        self.assertEqual(self.grid.lines_nb, 10)

    def test_cells_number(self):
        self.assertEqual(self.grid.cells_nb, 100)

    def test_rooms_number_and_type(self):
        self.assertEqual(self.grid.rooms_nb, 0)
        self.assertEqual(type(self.grid.rooms), list)

    def test_new_room_cells_not_integer(self):
        with self.assertRaises(ValueError):
            self.grid.add_room('x')
            self.grid.add_room(-1)

    def test_new_room_bad_cells_number(self):
        with self.assertRaises(AssertionError):
            self.grid.add_room(cells=1)
            self.grid.add_room(cells=100)

    def test_new_room_in_layout(self):
        new_room = self.grid.add_room(cells=SIZE['MIN_ROOM_CELLS'])
        self.assertEqual(self.grid.rooms_nb, 1)
        self.assertEqual(new_room.cells_nb, 4)

    def test_new_room_and_cells_ids(self):
        new_room = self.grid.add_room(cells=SIZE['MIN_ROOM_CELLS'])
        self.assertEqual(new_room.id, 0)
        self.assertEqual(new_room.cells[0].id, 0)
        self.assertEqual(new_room.cells[1].id, 1)
        self.assertEqual(new_room.cells[2].id, 2)
        self.assertEqual(new_room.cells[3].id, 3)

    def test_get_room_and_cell_by_id(self):
        self.grid.add_room(cells=SIZE['MIN_ROOM_CELLS'])
        the_room = self.grid.get_room(0)
        self.assertEqual(the_room.id, 0)
        the_cell = the_room.get_cell(2)
        self.assertEqual(the_cell.id, 2)
