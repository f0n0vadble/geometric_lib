import unittest

# Получает на вход длину стороны квадрата и возвращает его площадь по формуле a^2
def area(a):
    return a * a

# Получает на вход длину стороны квадрата и возвращает его периметр по формуле 4*a
def perimeter(a):
    return 4 * a

# Тесты для функций area и perimeter
class TestSquareFunctions(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5), 25.0)
        self.assertEqual(area(3), 9.0)
        self.assertEqual(area(0), 0.0)
        self.assertEqual(area(7.5), 56.25)

    def test_perimeter(self):
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(10), 40)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(7.5), 30.0)
