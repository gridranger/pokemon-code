from battleground import Battleground
from data import pokemons


class FightSimulator:
    _pokemon_list = list(pokemons.keys())

    @classmethod
    def run(cls):
        pokemon_output = cls._get_pokemon_output()
        protagonist = cls._get_protagonist(pokemon_output)
        antagonist = cls._get_antagonist(pokemon_output)
        battleground = Battleground(protagonist, antagonist)
        battleground.battle()

    @classmethod
    def _get_antagonist(cls, pokemon_output):
        antagonist_number = None
        while antagonist_number is None:
            antagonist_number = cls._filter_input(input(f"Enter the number of the enemy pokemon:\n{pokemon_output}"
                                                        "or 'x' to exit.\n# "))
        antagonist = pokemons[cls._pokemon_list[antagonist_number - 1]]
        print(f"Your enemy will be {antagonist.name}.")
        return antagonist

    @classmethod
    def _get_protagonist(cls, pokemon_output):
        protagonist_number = None
        while protagonist_number is None:
            protagonist_number = cls._filter_input(input(f"Enter the number of your pokemon:\n{pokemon_output}"
                                                         "or 'x' to exit.\n# "))
        protagonist = pokemons[cls._pokemon_list[protagonist_number - 1]]
        print(f"You picked {protagonist.name}.")
        return protagonist

    @classmethod
    def _get_pokemon_output(cls):
        pokemon_output = ""
        for index, name in enumerate(cls._pokemon_list):
            pokemon_output += f"  {index + 1}. {name}\n"
        return pokemon_output

    @staticmethod
    def _filter_input(user_input):
        error_message = f"Hint: please enter a valid number between 1 and {len(pokemons)}."
        if "x" in user_input.lower():
            exit()
        try:
            users_number = int(user_input)
        except ValueError:
            print(error_message)
            return None
        if 0 < users_number <= len(pokemons):
            return users_number
        else:
            print(error_message)
            return None


if __name__ == "__main__":
    FightSimulator.run()  # pragma no cover
