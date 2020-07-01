from unittest import TestCase
from unittest.mock import Mock
from battleground import Battleground


class DummyCreature():
    def __init__(self, name="a", current_health=100):
        self.name = name
        self.current_health = current_health
        self.is_fainted = False

    def __repr__(self):
        return self.name


class TestBattleGround(TestCase):
    def setUp(self):
        self.battleground = Battleground(DummyCreature(), DummyCreature())

    def _kill_antagonist(self):
        self.battleground._antagonist.is_fainted = True

    def test__calculate_damage(self):
        attacker, defender, effectiveness_multiplier = Mock(), Mock(), Mock()
        attacker.attack = 8
        defender.defense = 2
        effectiveness_multiplier.value = 0.5
        expected_value = Battleground.BASE_DAMAGE * 2
        result = self.battleground._calculate_damage(attacker, defender, effectiveness_multiplier)
        self.assertEqual(expected_value, result)

    def test__get_effectiveness_multiplyer(self):
        bigger, lower = Mock(), Mock()
        bigger.affinity = 2
        lower.affinity = 1
        self.assertEqual(2, self.battleground._get_effectiveness_multiplyer(bigger, lower).value)
        self.assertEqual(0.5, self.battleground._get_effectiveness_multiplyer(lower, bigger).value)
        self.assertEqual(1, self.battleground._get_effectiveness_multiplyer(bigger, bigger).value)

    def test__play_a_turn(self):
        fighter1, fighter2 = DummyCreature("a"), DummyCreature("b")
        self.battleground._get_effectiveness_multiplyer = Mock()
        self.battleground._calculate_damage = Mock(return_value=10)
        self.battleground._fighters = [fighter1, fighter2]
        self.battleground._play_a_turn()
        self.battleground._get_effectiveness_multiplyer.assert_called_once()
        self.battleground._calculate_damage.assert_called_once()
        self.assertEqual(90, fighter2.current_health)
        self.assertEqual([fighter2, fighter1], self.battleground._fighters)

    def test_battle(self):
        self.battleground._logger.info = Mock()
        self.battleground._play_a_turn = self._kill_antagonist
        self.battleground._announce_result = Mock()
        self.battleground.battle()
        self.battleground._announce_result.assert_called_once()

    def test__announce_result(self):
        self.battleground._logger.info = Mock()
        self.battleground._announce_result()
        self.battleground._logger.info.assert_called_with("Player won!")
        self.battleground._fighters.append(self.battleground._fighters.pop(0))
        self.battleground._announce_result()
        self.battleground._logger.info.assert_called_with("Opponent won!")
