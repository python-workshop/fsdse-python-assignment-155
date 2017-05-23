from unittest import TestCase


class TestSort(TestCase):
    def test_quick_sort(self):
        try:
            from build import sort
        except ImportError:
            self.assertFalse("no function found")

        print('None input')
        self.assertRaises(TypeError, sort, None)

        print('Empty input')
        self.assertEqual(sort([]), [])

        print('One element')
        self.assertEqual(sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        self.assertEqual(sort(data), sorted(data))