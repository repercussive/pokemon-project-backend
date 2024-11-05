from dataclasses import dataclass


@dataclass
class PokemonMultipleChoiceQuestion:
    """Represents a Who's That Pokémon?-style question.
    Returned from the "random-question" endpoint."""
    correct_pokemon_id: int
    correct_pokemon_image_url: str
    pokemon_name_options: list[str]


@dataclass
class AnswerResult:
    """Represents the response to the user's answer for a PokemonMultipleChoiceQuestion.
    Returned from the "verify-answer" endpoint."""
    correct_pokemon_name: str
    correct_pokemon_image_url: str
    is_correct: bool
