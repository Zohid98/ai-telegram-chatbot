import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from database.engine import create_db
from bot.handlers import message



bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(message.router)
async def main():

    await create_db()
    print("Bot ishga tushdi!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())