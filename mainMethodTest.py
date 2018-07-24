import unittest
import mainMethod


class TestMainMethod(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, mainMethod.add(2, 3))

        self.assertNotEqual(15, mainMethod.add(5, 3))

    def test_subtract(self):
        self.assertEqual(10, mainMethod.subtract(15, 5))

    def test_is_higher_than_ten(self):
        self.assertTrue(mainMethod.is_higher_than_ten(13))

        self.assertFalse(mainMethod.is_higher_than_ten(10))

        self.assertFalse(mainMethod.is_higher_than_ten(5))

    def test_check_add_operation(self):
        self.assertTrue(mainMethod.check_for_add_operation('a'))
        self.assertTrue(mainMethod.check_for_add_operation('A'))

        self.assertFalse(mainMethod.check_for_add_operation('s'))

    def test_check_subtraction_operation(self):
        self.assertTrue(mainMethod.check_for_subtract_operation('s'))
        self.assertTrue(mainMethod.check_for_subtract_operation('S'))

        self.assertFalse(mainMethod.check_for_subtract_operation('t'))