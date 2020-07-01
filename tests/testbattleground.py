from unittest import TestCase
from data import pokemons
from battleground import Battleground


class TestBattleGround(TestCase):
    def test_battle_user_win(self):
        battleground = Battleground(pokemons["Bulbasaur"], pokemons["Squirtle"])
        battleground.battle()

    def test_battle_opponent_win(self):
        battleground = Battleground(pokemons["Bulbasaur"], pokemons["Pikachu"])
        battleground.battle()
