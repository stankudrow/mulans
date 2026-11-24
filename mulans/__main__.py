import asyncio

from mulans import AsyncClient, Translator


async def main() -> None:
    client = AsyncClient(model="qwen3-trans")
    translator = Translator(client)
    answer = await translator.translate("Привет, как тебя зовут?")
    print(answer)


asyncio.run(main())
