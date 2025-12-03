import unittest

# Получает на вход длины сторон прямоугольника и возвращает его площадь по формуле a*b
def area(a,b):
    return a * b

# Получает на вход длины сторон прямоугольника и возвращает его периметр по формуле 2*(a+b)
def perimeter(a,b):
    return 2 * (a + b)

# Тесты для функций area и perimeter
class TestRectangleFunctions(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(10, 5), 50.0)
        self.assertEqual(area(3, 4), 12.0)
        self.assertEqual(area(0, 5), 0.0)
        self.assertEqual(area(7.5, 2.5), 18.75)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4), 14)
        self.assertEqual(perimeter(10, 10), 40)
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(7.5, 2.5), 20.0)

    