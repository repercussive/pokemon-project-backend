import asyncio
from .http_client import HttpClient


async def fetch_json_single(url: str) -> dict:
    client = HttpClient.get_aiohttp_client()
    async with client.get(url) as response:
        return await response.json()


async def fetch_json_many(urls: list[str]) -> list[dict]:
    return await asyncio.gather(*[fetch_json_single(url) for url in urls])
