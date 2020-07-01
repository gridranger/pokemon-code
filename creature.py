from affinities import Affinities


class Creature():
    def __init__(self, initializer_json=None):
        if initializer_json is None:
            self.name = "Dummymon"
            self.health = 100
            self.attack = 10
            self.defense = 10
            self.affinity = Affinities.NEUTRAL
        elif {"name", "health", "attack", "defense", "affinity"} == initializer_json.keys():
            self.__dict__.update(initializer_json)
        else:
            raise RuntimeError("A wild invalid initializer JSON appeared!")
        self.current_health = self.health

    @property
    def is_fainted(self):
        return self.current_health <= 0

    def __str__(self):
        return f"{self.name} (HP: {self.current_health})"
