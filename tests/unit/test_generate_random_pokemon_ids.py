import pytest
from src.utils.pokemon import generate_random_pokemon_ids


@pytest.mark.parametrize("expected_ids_count", [4, 50, 151])
def test_generates_correct_number_of_pokemon_ids(expected_ids_count):
    random_ids = generate_random_pokemon_ids(expected_ids_count)
    assert len(random_ids) == expected_ids_count


def test_generates_unique_pokemon_ids():
    random_ids = generate_random_pokemon_ids(151, 151)
    assert len(random_ids) == len(set(random_ids))


def test_generates_pokemon_ids_within_expected_range():
    random_ids = generate_random_pokemon_ids(4, 4)
    assert not set.difference(set(random_ids), {1, 2, 3, 4})
