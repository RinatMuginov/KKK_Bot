from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from helpers import check_in_admins
from config import API_TOKEN, CHANNEL_ID, ADMINS

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_bot(message: Message):
    await message.answer(
        "Привет, я маленький негр, который служит ККК\n"
        "Команды:\n"
        "/ping — постинг pong в изгойду\n"
        "/test_post — запостить тест пост в изгойду\n"
    )

@dp.message(Command("ping"))
async def ping_handler(message: Message):
    if not check_in_admins(message.from_user.id, ADMINS):
        await message.answer("Нет доступа")
    else:
        await message.answer("pong")
        await bot.send_message(CHANNEL_ID, "pong")

#@dp.message(Command("debug_chat_id"))
#async def debug_chat_id_handler(message: Message):
#    await message.answer(f"chat_id этого чата: {message.chat.id}")

@dp.message(Command("test_post"))
async def test_post(message: Message):
    if not check_in_admins(message.from_user.id, ADMINS):
        await message.answer("Нет доступа")
    else:
        await bot.send_message(CHANNEL_ID, "Это пост в канале!")
        await message.answer("Я отправил пост в канал Изгойда")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())