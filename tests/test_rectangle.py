import pytest

import source.shapes
import source.shapes as shapes

# moved fixtures to conftest.py
# @pytest.fixture
# def my_rectangle():
#     return shapes.Rectangle(10, 20)
#
# @pytest.fixture
# def weird_rectangle():
#     return shapes.Rectangle(5,6)

# with pytest fixture
def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20


# without pytest fixture
# def test_area():
#     rectangle = shapes.Rectangle(10, 20)
#     assert rectangle.area() == 10 * 20

# with pytest fixture
def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 60

# without pytest fixture
# def test_perimeter():
#     rectangle = shapes.Rectangle(10,20)
#     assert rectangle.perimeter() == 60

def test_not_equal(my_rectangle,weird_rectangle):
    assert my_rectangle != weird_rectangle

