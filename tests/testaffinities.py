from unittest import TestCase
from affinities import Affinities


class TestAffinities(TestCase):
    def test_is_effective_against(self):
        self.assertTrue(Affinities.FIRE._is_effective_against(Affinities.GRASS))
        self.assertFalse(Affinities.WATER._is_effective_against(Affinities.ELECTRIC))

    def test_is_ineffective_against(self):
        self.assertTrue(Affinities.WATER._is_ineffective_against(Affinities.GRASS))
        self.assertFalse(Affinities.ELECTRIC._is_ineffective_against(Affinities.FIRE))

    def test___eq__(self):
        self.assertTrue(Affinities.FIRE == Affinities.ELECTRIC)
        self.assertFalse(Affinities.WATER == Affinities.GRASS)

    def test___lt__(self):
        self.assertTrue(Affinities.WATER < Affinities.ELECTRIC)

    def test___gt__(self):
        self.assertTrue(Affinities.WATER > Affinities.FIRE)
