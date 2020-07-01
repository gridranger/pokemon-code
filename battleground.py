from logging import basicConfig, getLogger, INFO
from math import floor
from random import shuffle
from effectiveness import Effectivness

basicConfig(level=INFO)


class Battleground:
    BASE_DAMAGE = 50

    def __init__(self, protagonist, antagonist):
        self._protagonist = protagonist
        self._antagonist = antagonist
        self._fighters = [self._protagonist, self._antagonist]
        self._logger = getLogger(__name__)

    def battle(self):
        self._logger.info(f"A wild {self._antagonist.name} appeared!")
        self._logger.info(f"Player: {self._protagonist.name}, I choose you!")
        shuffle(self._fighters)
        self._logger.info(f"{self._fighters[0].name} starts the fight.")
        while not any(pokemon.is_fainted for pokemon in self._fighters):
            self._play_a_turn()
        self._logger.info(f"{self._fighters[1].name} is fainted!")
        self._logger.info(f"The winner is: {self._fighters[0].name}!")
        self._announce_result()

    def _announce_result(self):
        if self._fighters[0] is self._protagonist:
            self._logger.info("Player won!")
        else:
            self._logger.info("Opponent won!")

    def _play_a_turn(self):
        attacker = self._fighters[0]
        defender = self._fighters[1]
        self._logger.info(f"{attacker} attacks...")
        effectiveness_multiplier = self._get_effectiveness_multiplyer(attacker, defender)
        self._logger.info(f"...its {effectiveness_multiplier.name.replace('_', ' ')}.")
        damage = self._calculate_damage(attacker, defender, effectiveness_multiplier)
        self._logger.info(f"{attacker} damages {defender.name} for {damage} points!")
        defender.current_health -= damage
        if not defender.is_fainted:
            self._fighters.append(self._fighters.pop(0))

    def _calculate_damage(self, attacker, defender, effectiveness_multiplier):
        return floor(self.BASE_DAMAGE * (attacker.attack / defender.defense) * effectiveness_multiplier.value)

    def _get_effectiveness_multiplyer(self, attacker, defender):
        if attacker.affinity > defender.affinity:
            effectiveness_multiplier = Effectivness.super_effective
        elif attacker.affinity < defender.affinity:
            effectiveness_multiplier = Effectivness.not_very_effective
        else:
            effectiveness_multiplier = Effectivness.effective
        return effectiveness_multiplier
