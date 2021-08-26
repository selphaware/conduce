import unittest
from src.conduce.conduce import read_yaml, read_json


class TestConduce(unittest.TestCase):

    def test_yaml(self):
        cfg = read_yaml("test.yaml", "tests")
        self.assertEqual(cfg('alpha.beta.gamma'), 45613)
        self.assertEqual(len(cfg('alpha.beta.delta')), 8)

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

    def test_nstruct_yaml(self):
        cfg = read_yaml("test.yaml", "tests", type_obj=True)
        self.assertEqual(cfg.alpha.beta.delta[7].phi.beta[3].rho.zelda[2].polo, "hello world again")

    def test_nstruct_json(self):
        cfg = read_json("test.json", "tests", type_obj=True)
        self.assertEqual(cfg.alpha.beta.epsilon.phi[3].hello, "world")

    def test_deep_yaml(self):
        cfg = read_yaml("some_deep_nested.yaml", "tests", type_obj=True)
        self.assertEqual(cfg.alpha.hello[3].rho[2].fellow, "end of the road")


if __name__ == '__main__':
    unittest.main()
