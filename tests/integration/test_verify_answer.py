import pytest
from src.main import app
from httpx import AsyncClient, ASGITransport
from unittest.mock import AsyncMock


# ? ===== Reusable helper for testing. Assumes correct answer is "Bulbasaur" =====
async def verify_answer_helper(mocker, guessed_pokemon_name: str, expected_response: dict):
    mock_fetch_json_single = AsyncMock(return_value={
        "name": "bulbasaur", "sprites": {"front_default": "bulbasaur_image_url"}
    })
    mocker.patch("src.main.fetch_json_single", mock_fetch_json_single)

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get(f"/verify-answer?correct_pokemon_id=1&guessed_pokemon_name={guessed_pokemon_name}")

    assert response.status_code == 200
    assert response.json() == expected_response


@pytest.mark.asyncio
async def test_verify_answer_works_when_user_is_correct(mocker):
    guessed_pokemon_name = "bulbasaur"
    await verify_answer_helper(mocker, guessed_pokemon_name, expected_response={
        "is_correct": True,
        "correct_pokemon_image_url": "bulbasaur_image_url",
        "correct_pokemon_name": "bulbasaur"
    })


@pytest.mark.asyncio
async def test_verify_answer_is_case_insensitive(mocker):
    guessed_pokemon_name = "bUlBaSaUr"
    await verify_answer_helper(mocker, guessed_pokemon_name, expected_response={
        "is_correct": True,
        "correct_pokemon_image_url": "bulbasaur_image_url",
        "correct_pokemon_name": "bulbasaur"
    })


@pytest.mark.asyncio
async def test_verify_answer_works_when_user_is_incorrect(mocker):
    guessed_pokemon_name = "charmander"
    await verify_answer_helper(mocker, guessed_pokemon_name, expected_response={
        "is_correct": False,
        "correct_pokemon_image_url": "bulbasaur_image_url",
        "correct_pokemon_name": "bulbasaur"
    })
