
import asyncio
from servis.history_servis import prepare_history
from database.models.requests import get_user_messages, save_message
from google import genai
from config import GEMINI_API_KEY

async def get_history(user_id):
    messages = await get_user_messages(user_id = user_id)
    history = prepare_history(messages)
    return history
async def generate_answer(user_id, user_message):
    await save_message(user_id=user_id,role="user", content=user_message)
    history = await get_history(user_id=user_id)
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = await client.aio.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents= history

    )
    # GEMINI JAVOBINI BAZAGA SAQLASH
    await save_message(
        user_id=user_id,
        role="assistant",
        content=response.text
    )
    return response.text

async def main():
    answer = await generate_answer(
        user_id=1,
        user_message="Mening ismim nima?!"
    )

    print(answer)


if __name__ == '__main__':
    asyncio.run(main())