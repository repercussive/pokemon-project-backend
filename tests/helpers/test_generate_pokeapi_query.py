from src.utils.pokemon import generate_pokeapi_query


def test_generates_correct_pokeapi_query_url():
    query_url = generate_pokeapi_query(123)
    assert query_url == "https://pokeapi.co/api/v2/pokemon/123"
