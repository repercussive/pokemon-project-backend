# Who's That Pokémon? (Back-end)

This repository stores project files for the back-end "Who's That Pokémon" API. This app is developed with:

- Python
- FastAPI
- aiohttp (for asynchronous network requests)
- Pytest

### Contents

- [Running the app locally](#running-the-app-locally)
  - [Running tests](#running-tests)
  - [Quick API reference](#quick-api-reference)
    - [`/random-question` endpoint](#random-question-endpoint)
      - [Example:](#example)
    - [`/verify-answer` endpoint](#verify-answer-endpoint)
      - [Example 1 (correct answer):](#example-1-correct-answer)
      - [Example 2 (incorrect answer):](#example-2-incorrect-answer)

---

This application complements the front-end application. [Click here to view details on running the front-end app](https://github.com/repercussive/pokemon-project-frontend).

## Running the app locally

To run the application, you must have Python 3.12+ installed. Python releases can be found here: https://www.python.org/downloads/

Once you have cloned the repository, it is strongly recommended to create a Python [virtual environment](https://docs.python.org/3/library/venv.html) to isolate package installations.

- Virtual environment guidance for VS Code: https://code.visualstudio.com/docs/python/environments
- Virtual environment guidance for PyCharm: https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env

With this complete, open a terminal in the repository's root directory. Then, to install the application's dependencies, execute the following command:

```
pip install -e .
```

You can now run the FastAPI application. To run it in development, execute the following command:

```
fastapi dev src/main.py
```

👉 The application will be exposed on http://localhost:8000/
👉 To view interactive API documentation (Swagger), visit http://localhost:8000/docs

For production use, execute `fastapi run src/main.py` instead.

## Running tests

To run tests, execute the following command:

```
python -m pytest
```

## Quick API reference

The API exposes 2 endpoints, `/random-question` and `/verify-answer`.

### `/random-question` endpoint

- Receives no query parameters.
- Returns JSON data representing a multiple-choice "Who's That Pokémon?" question

#### Example:

- Request: `/random-question`
- Example response:

```json
{
  "correctPokemonId": 99,
  "correctPokemonImageUrl": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/99.png",
  "pokemonNameOptions": ["kingler", "aerodactyl", "kakuna", "spearow"]
}
```

---

### `/verify-answer` endpoint

- Receives 2 query parameters:
  1. `correct_pokemon_id` (integer): _the ID of a Pokémon_
  2. `guessed_pokemon_name` (string): _a Pokémon name, which may or may not match the `correct_pokemon_id`_
- Returns JSON data including:
  - The true name of the Pokémon, corresponding to `correct_pokemon_id`
  - Image URL of the correct Pokémon
  - A boolean property `isCorrect`, which represents whether `guessed_pokemon_name` matched `correct_pokemon_id`

#### Example 1 (correct answer):

- Request: `/verify-answer?correct_pokemon_id=1&guessed_pokemon_name=Bulbasaur`
- Response:

```json
{
  "correctPokemonName": "bulbasaur",
  "correctPokemonImageUrl": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
  "isCorrect": true
}
```

#### Example 2 (incorrect answer):

- Request: `/verify-answer?correct_pokemon_id=1&guessed_pokemon_name=Venusaur`
- Response:

```json
{
  "correctPokemonName": "bulbasaur",
  "correctPokemonImageUrl": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
  "isCorrect": false
}
```
