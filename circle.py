import unittest

import math

# Получает на вход радиус круга и возвращает его площадь по формуле π*r^2
def area(r):
    return math.pi * r * r

# Получает на вход радиус круга и возвращает его периметр по формуле 2*π*r
def perimeter(r):
    return 2 * math.pi * r

# Тесты для функций area и perimeter
class TestCircleFunctions(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(5), 78.53981633974483)
        self.assertAlmostEqual(area(3), 28.274333882308138)
        self.assertAlmostEqual(area(0), 0.0)
        self.assertAlmostEqual(area(7.5), 176.71458676442586)
        self.assertAlmostEqual(area(7.5), 176.71458676)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(5), 31.41592653589793)
        self.assertAlmostEqual(perimeter(10), 62.83185307179586)
        self.assertAlmostEqual(perimeter(0), 0.0)
        self.assertAlmostEqual(perimeter(7.5), 47.12388980384689)
        self.assertAlmostEqual(perimeter(7.5), 47.1238898)