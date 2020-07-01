from unittest import TestCase
from creature import Creature


class TestCreature(TestCase):
    def test_basic_init(self):
        c = Creature()
        self.assertEqual("Dummymon", c.name)

    def test_json_init(self):
        c = Creature({"name": "Magicarp", "health": 10, "attack": 1, "defense": 10, "affinity": "water"})
        self.assertEqual("Magicarp", c.name)

    def test_failed_init(self):
        with self.assertRaises(RuntimeError) as e:
            Creature({"name": "Magicarp", "health": 10, "attack": 1, "defense": 10})
        self.assertEqual(e.exception.args[0], "A wild invalid initializer JSON appeared!")
