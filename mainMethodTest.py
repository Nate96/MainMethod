import unittest
from mainMethod import object


class TestMainMethod(unittest.TestCase):
    def setUp(self):
        self.object = object()

    def test_add(self):
        self.assertEqual(5, self.object.add_(2, 3))

        self.assertNotEqual(15, self.object.add_(5, 3))

    def test_is_higher_than_ten_(self):
        self.assertTrue(object.is_higher_than_ten_(13))

        self.assertFalse(object.is_higher_than_ten_(10))

        self.assertFalse(object.is_higher_than_ten_(5))

