import re

from mulans.client import AsyncClient

__all__ = ["Translator"]




class Translator:
    def __init__(self, client: AsyncClient) -> None:
        self._c = client

    async def translate(self, text: str) -> str:
        response = await self._c.send(text)
        return response.get()
