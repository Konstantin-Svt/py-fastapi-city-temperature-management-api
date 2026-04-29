from typing import AsyncGenerator

from httpx import AsyncClient


async def get_client() -> AsyncGenerator:
    client = AsyncClient()
    try:
        yield client
    finally:
        await client.aclose()
