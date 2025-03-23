from openai import AsyncOpenAI
from config import Config


client = AsyncOpenAI(api_key=Config.OPENAI_API_KEY)


async def analyze(contract):
    try:
        response = await client.responses.create(
            model="gpt-3.5-turbo",
            input="Write a one-sentence bedtime story about a unicorn.",
            # instructions=Config.INSTRUCTIONS,
            # input=f"analyze this contract: {contract}",
        )
        return response.output_text
    except Exception as e:
        print(f"Error from OpenAI: {e}")
