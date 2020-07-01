from logging import basicConfig, getLogger, INFO, info
from math import floor
from random import shuffle
from effectiveness import Effectivness

basicConfig(level=INFO)


class Battleground:
    def __init__(self, protagonist, antagonist):
        self.protagonist = protagonist
        self.antagonist = antagonist
        self.fighters = [self.protagonist, self.antagonist]
        self.logger = getLogger(__name__)

    def battle(self):
        info(f"A wild {self.antagonist.name} appeared!")
        info(f"Player: {self.protagonist.name}, I choose you!")
        shuffle(self.fighters)
        info(f"{self.fighters[0].name} starts the fight.")
        while not any(pokemon.is_fainted for pokemon in self.fighters):
            self._play_a_turn()
        info(f"{self.fighters[1].name} is fainted!")
        info(f"The winner is: {self.fighters[0].name}!")
        if self.fighters[0] is self.protagonist:
            info("Player won!")
        else:
            info("Opponent won!")

    def _play_a_turn(self):
        attacker = self.fighters[0]
        defender = self.fighters[1]
        info(f"{attacker} attacks...")
        effectiveness_multiplier = self._get_effectiveness_multiplyer(attacker, defender)
        info(f"...its {effectiveness_multiplier.name.replace('_', ' ')}.")
        damage = self._calculate_damage(attacker, defender, effectiveness_multiplier)
        info(f"{attacker} damages {defender.name} for {damage} points!")
        defender.current_health -= damage
        if not defender.is_fainted:
            self.fighters.append(self.fighters.pop(0))

    def _calculate_damage(self, attacker, defender, effectiveness_multiplier):
        return floor(50 * (attacker.attack / defender.defense) * effectiveness_multiplier.value)

    def _get_effectiveness_multiplyer(self, attacker, defender):
        if attacker.affinity > defender.affinity:
            effectiveness_multiplier = Effectivness.super_effective
        elif attacker.affinity < defender.affinity:
            effectiveness_multiplier = Effectivness.not_very_effective
        else:
            effectiveness_multiplier = Effectivness.effective
        return effectiveness_multiplier
