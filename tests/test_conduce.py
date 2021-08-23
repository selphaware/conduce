import unittest
from src.conduce.conduce import read_yaml, read_json


class TestConduce(unittest.TestCase):

    def test_yaml(self):
        cfg = read_yaml("test.yaml", "tests")
        self.assertEqual(cfg('alpha.beta.gamma'), 45613)
        self.assertEqual(len(cfg('alpha.beta.delta')), 7)

    def test_json(self):
        cfg = read_json("test.json", "tests")
        self.assertEqual(cfg('alpha.beta.gamma'), 25618)
        self.assertEqual(len(cfg('alpha.beta.delta')), 9)

    def test_empty_key_json(self):
        cfg = read_json("test.json", "tests")
        self.assertEqual(list(cfg().keys())[0], "alpha")

    def test_empty_key_yaml(self):
        cfg = read_yaml("test.yaml", "tests")
        self.assertEqual(list(cfg().keys())[0], "alpha")


if __name__ == '__main__':
    unittest.main()
