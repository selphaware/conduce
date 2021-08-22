import unittest
from src.conduce.conduce import read_yaml


class TestConduce(unittest.TestCase):

    def test_yaml(self):
        cfg = read_yaml("test.yaml", "tests")
        self.assertEqual(cfg('alpha.beta.gamma'), 45613)
        self.assertEqual(len(cfg('alpha.beta.delta')), 7)


if __name__ == '__main__':
    unittest.main()
