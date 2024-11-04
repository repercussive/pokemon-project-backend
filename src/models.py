from dataclasses import dataclass


@dataclass
class PokemonMultipleChoiceQuestion:
    correct_pokemon_id: int
    correct_pokemon_image_url: str
    pokemon_name_options: list[str]
