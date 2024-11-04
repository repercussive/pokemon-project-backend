import random


def generate_random_pokemon_ids(number_of_ids=4, max_id=151) -> list[int]:
    return random.sample(range(1, max_id + 1), number_of_ids)
