import pytest
from src.main import app
from httpx import AsyncClient, ASGITransport
from unittest.mock import AsyncMock


@pytest.mark.asyncio
async def test_random_question_endpoint(mocker):
    mocker.patch(
        "src.main.generate_random_pokemon_ids",
        return_value=[1, 2, 3, 4])

    mock_fetch_json_many = AsyncMock(return_value=[
        {"name": "bulbasaur", "sprites": {"front_default": "bulbasaur_image_url"}},
        {"name": "ivysaur", "sprites": {"front_default": "ivysaur_image_url"}},
        {"name": "venusaur", "sprites": {"front_default": "venusaur_image_url"}},
        {"name": "charmander", "sprites": {"front_default": "charmander_image_url"}}
    ])
    mocker.patch("src.main.fetch_json_many", mock_fetch_json_many)

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/random-question")

    assert response.status_code == 200

    assert response.json() == {
        "correct_pokemon_id": 1,
        "correct_pokemon_image_url": "bulbasaur_image_url",
        "pokemon_name_options": [
            "bulbasaur", "ivysaur", "venusaur", "charmander"
        ]
    }
