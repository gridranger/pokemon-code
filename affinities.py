from enum import auto
from autonamedenum import AutoNamedEnum


class Affinities(AutoNamedEnum):
    NEUTRAL = auto()
    FIRE = auto()
    WATER = auto()
    GRASS = auto()
    ELECTRIC = auto()

    @classmethod
    def _you_could_beat_with(cls):
        return {cls.FIRE.value: [cls.GRASS.value],
                cls.WATER.value: [cls.FIRE.value],
                cls.GRASS.value: [cls.WATER.value],
                cls.ELECTRIC.value: [cls.WATER.value]}

    def _is_effective_against(self, other):
        you_could_beat_with = self._you_could_beat_with()
        return other.value in you_could_beat_with[self.value]

    def _is_ineffective_against(self, other):
        you_could_beat_with = self._you_could_beat_with()
        for overwhelming, overwhelmed_ones in you_could_beat_with.items():
            if self.value in overwhelmed_ones and other.value is overwhelming:
                return True
        return False

    def __eq__(self, other):
        return not self.__ne__(other)

    def __ne__(self, other):
        return self._is_effective_against(other) or self._is_ineffective_against(other)

    def __lt__(self, other):
        return self._is_ineffective_against(other)

    def __gt__(self, other):
        return self._is_effective_against(other)
