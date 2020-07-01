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

    def test_is_fainted(self):
        c = Creature()
        self.assertFalse(c.is_fainted)
        c.current_health = -1
        self.assertTrue(c.is_fainted)

    def test____repr__(self):
        c = Creature()
        self.assertEqual("Dummymon (HP: 100)", f"{c}")
