import asyncio

from aiogram import Bot, Dispatcher

from hendlers import *

token_ai = "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" # Не трогать
token_bot = "8244062672:AAEF1BxLpx6HHfekvwJJ1V4lrjENx2r_Q9c" # получи токен в @BotFather

async def main():
    bot = Bot(token=token_bot)
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

