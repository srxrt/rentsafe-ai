from openai import AsyncOpenAI
from config import Config


client = AsyncOpenAI(api_key=Config.OPENAI_API_KEY)


async def analyze(contract):
    response = await client.responses.create(
        model="gpt-3.5-turbo",
        instructions=Config.INSTRUCTIONS,
        input=f"analyze this contract: {contract}",
    )
    return response.output_text
