import unittest

# Получает на вход основание и высоту треугольника и возвращает его площадь
def area(a, h):
    return 0.5 * a * h

# Получает на вход длины сторон треугольника и возвращает его периметр
def perimeter(a, b, c):
    return a + b + c

# Тесты для функций area и perimeter
class TestTriangleFunctions(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(10, 5), 25.0)
        self.assertAlmostEqual(area(3, 4), 6.0)
        self.assertAlmostEqual(area(0, 5), 0.0)
        self.assertAlmostEqual(area(7.5, 2.5), 9.375)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(10, 10, 10), 30)
        self.assertEqual(perimeter(0, 5, 5), 10)
        self.assertEqual(perimeter(7.5, 2.5, 5), 15.0)