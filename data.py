from affinities import Affinities
from creature import Creature

_raw_pokemon_data = [{"name": "Charmeleon", "health": 110, "attack": 75, "defense": 55, "affinity": Affinities.FIRE},
                     {"name": "Squirtle", "health": 90, "attack": 65, "defense": 40, "affinity": Affinities.WATER},
                     {"name": "Bulbasaur", "health": 70, "attack": 60, "defense": 65, "affinity": Affinities.GRASS},
                     {"name": "Pikachu", "health": 80, "attack": 80, "defense": 80, "affinity": Affinities.ELECTRIC},
                     {"name": "Magicarp", "health": 50, "attack": 5, "defense": 50, "affinity": Affinities.WATER}]

pokemons = {record["name"]: Creature(record) for record in _raw_pokemon_data}
