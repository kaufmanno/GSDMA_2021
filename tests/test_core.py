import unittest
from .context import GSDMA_2021


class CoreTestCase(unittest.TestCase):
    def test_fake_function(self):
        actual = GSDMA_2021.core.fake_function()
        expected = "Hello world!"
        self.assertEqual(expected, actual)

    def test(self):
        fake = GSDMA_2021.core.FakeClass();
        actual = fake.name
        expected = 'unknown'
        self.assertEqual(expected, actual)
        fake = GSDMA_2021.core.FakeClass(name="test")
        actual = fake.name
        expected = 'test'
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
