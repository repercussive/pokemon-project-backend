import asyncio
import aiohttp


async def fetch(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def fetch_all(urls: list[str]):
    return await asyncio.gather(*[fetch(url) for url in urls])
