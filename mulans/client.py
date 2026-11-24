import re

from ollama import AsyncClient as AsyncOllamaClient
from ollama import ChatResponse

__all__ = ["AsyncClient"]


_THINK_RE = re.compile(r"</?think>|^\s+$")


class Response:
    def __init__(self, response: ChatResponse) -> None:
        self._r = response

    def get(self) -> str:
        answer = self._r["message"]["content"]
        return _THINK_RE.sub("", answer)


class AsyncClient:
    def __init__(self, *, model: str) -> None:
        self._client = AsyncOllamaClient()
        self._model = model

    async def send(self, text: str) -> Response:
        response: ChatResponse = await self._client.chat(
            model=self._model,
            messages=[{"role": "user", "content": text}],
            think=False,
        )
        return Response(response)
