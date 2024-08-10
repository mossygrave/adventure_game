import csv
from basic_functions import move, directions
import pytest

#Directions is incomplete at the moment and will not have a test function yet
#Functions have to be tested on my laptop because it has the proper files

def test_move():

    assert move(3, "north") == 7
    assert move(8, "south") == 4
    assert move(2, "east") == 3
    assert move(2, "west") == 1


doors = {
    "North" : [10, 11, 3, 8, 5, 4, 1],
    "East" : [13, 6, 14, 7, 9, 10, 11, 3, 1, 2],
    "South" : [14, 7, 9, 12, 15, 8, 5],
    "West" : [14, 7, 12, 15, 10, 11, 3, 8, 4, 2]
}

def test_directions():

    assert directions(1, doors) == ["NORTH", "EAST"]
    assert directions(2, doors) == ["EAST", "WEST"]
    assert directions(3, doors) == ["NORTH", "EAST", "WEST"]
    assert directions(4, doors) == ["NORTH", "WEST"]
    assert directions(5, doors) == ["NORTH", "SOUTH"]
    assert directions(6, doors) == ["EAST"]
    assert directions(7, doors) == ["EAST", "SOUTH", "WEST"]
    assert directions(8, doors) == ["NORTH", "SOUTH", "WEST"]
    assert directions(9, doors) == ["EAST", "SOUTH"]
    assert directions(10, doors) == ["NORTH", "EAST", "WEST"]
    assert directions(11, doors) == ["NORTH", "EAST", "WEST"]
    assert directions(12, doors) == ["SOUTH", "WEST"]
    assert directions(13, doors) == ["EAST"]
    assert directions(14, doors) == ["EAST", "SOUTH", "WEST"]
    assert directions(15, doors) == ["SOUTH", "WEST"]
    



pytest.main(["-v", "--tb=line", "-rN", __file__])