import random
from models import PokemonMultipleChoiceQuestion, AnswerResult
from utils.pokemon import generate_random_pokemon_ids, generate_pokeapi_query
from utils.http_client import HttpClient
from utils.fetch import fetch_json_single, fetch_json_many
from fastapi import FastAPI
from contextlib import asynccontextmanager

app = FastAPI()


@asynccontextmanager
async def lifespan():
    HttpClient.get_aiohttp_client()
    yield
    await HttpClient.close_aiohttp_client()


@app.get("/random-question")
async def random_question() -> PokemonMultipleChoiceQuestion:
    pokemon_ids = generate_random_pokemon_ids(number_of_ids=4, max_id=151)
    pokeapi_urls = [generate_pokeapi_query(id) for id in pokemon_ids]
    pokemon_list = await fetch_json_many(pokeapi_urls)
    pokemon_name_options = [pokemon["name"] for pokemon in pokemon_list]
    random.shuffle(pokemon_name_options)

    return PokemonMultipleChoiceQuestion(
        correct_pokemon_id=pokemon_ids[0],
        correct_pokemon_image_url=pokemon_list[0]["sprites"]["front_default"],
        pokemon_name_options=pokemon_name_options
    )


@app.get("/verify-answer")
async def verify_answer(correct_pokemon_id: int, guessed_pokemon_name: str) -> AnswerResult:
    correct_pokemon = await fetch_json_single(generate_pokeapi_query(correct_pokemon_id))
    correct_pokemon_name = correct_pokemon["name"]

    return AnswerResult(
        is_correct=correct_pokemon_name.casefold() == guessed_pokemon_name.casefold(),
        correct_pokemon_image_url=correct_pokemon["sprites"]["front_default"],
        correct_pokemon_name=correct_pokemon_name
    )
