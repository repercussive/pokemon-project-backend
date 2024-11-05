from utils.pokemon import generate_random_pokemon_ids
from utils.http_client import HttpClient
from utils.fetch import fetch_json_many
from models import PokemonMultipleChoiceQuestion
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
    pokeapi_urls = [
        f"https://pokeapi.co/api/v2/pokemon/{id}"
        for id in pokemon_ids
    ]

    all_pokemon = await fetch_json_many(pokeapi_urls)

    return PokemonMultipleChoiceQuestion(
        correct_pokemon_id=pokemon_ids[0],
        correct_pokemon_image_url=all_pokemon[0]["sprites"]["front_default"],
        pokemon_name_options=[pokemon["name"] for pokemon in all_pokemon]
    )
