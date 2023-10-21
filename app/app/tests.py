"""
Sample test file
"""

from django.test import SimpleTestCase

from app.calculate import add, subtract


class AddTestCase(SimpleTestCase):
    def test_add_numbers(self):
        result = add(5, 6)
        self.assertEqual(result, 11)

    def test_subtract_numbers(self):
        result = subtract(10, 15)
        self.assertEqual(result, 5)
