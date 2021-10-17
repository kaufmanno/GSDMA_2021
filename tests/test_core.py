import unittest
from .context import gsdma_2021 as gsdma


class CoreTestCase(unittest.TestCase):
    def test_fake_function(self):
        actual = gsdma.core.fake_function()
        expected = "Hello world!"
        self.assertEqual(expected, actual)

    def test(self):
        fake = gsdma.core.FakeClass();
        actual = fake.name
        expected = 'unknown'
        self.assertEqual(expected, actual)
        fake = gsdma.core.FakeClass(name="test")
        actual = fake.name
        expected = 'test'
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
