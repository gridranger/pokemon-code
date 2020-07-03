from unittest import TestCase
from unittest.mock import Mock, patch
from fightsimulator import FightSimulator


class TestFightSimulator(TestCase):

    @patch("battleground.Battleground.battle")
    def test_run(self, b):
        f = FightSimulator
        f._get_pokemon_output = Mock()
        f._get_protagonist = Mock()
        f._get_antagonist = Mock()
        FightSimulator.run()
        f._get_pokemon_output.assert_called_once()
        f._get_protagonist.assert_called_once()
        f._get_antagonist.assert_called_once()
        b.assert_called_once()

    @patch("builtins.input", return_value="1")
    def test__get_antagonist(self, i):
        result = FightSimulator._get_antagonist("")
        self.assertTrue(result.affinity)

    @patch("builtins.input", return_value="1")
    def test__get_protagonist(self, i):
        result = FightSimulator._get_protagonist("")
        self.assertTrue(result.affinity)

    def test__get_pokemon_output(self):
        self.assertTrue(". Charmeleon" in FightSimulator._get_pokemon_output())

    @patch("builtins.exit")
    def test__filter_input(self, e):
        FightSimulator._filter_input("x")
        e.assert_called_once()
        self.assertEqual(1, FightSimulator._filter_input("1"))
        self.assertIsNone(FightSimulator._filter_input("0"))
        self.assertIsNone(FightSimulator._filter_input("foo"))
