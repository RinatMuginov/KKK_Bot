from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from helpers import check_in_admins
from config import API_TOKEN, CHANNEL_ID, ADMINS
import asyncio
from aiogram.fsm.context import FSMContext
from models import Cinema, CinemaForm, TwoWeeksCinema, TwoWeeksCinemaForm

not_access_message="Нет доступа, шел на хуй"

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

@dp.message(Command("create_week"))
async def process_title(message: Message, state: FSMContext):
    if not check_in_admins(message.from_user.id, ADMINS): await message.answer(not_access_message)
    else:
        await state.set_state(TwoWeeksCinemaForm.waiting_for_title)
        await message.answer("Введите название недели в формате ДВЕ НЕДЕЛИ КОГО/ЧЕГО (Например, две недели Стэнли Кубрика)") #добавить эксцепты

@dp.message(TwoWeeksCinemaForm.waiting_for_title)
async def process_date_of_start(message: Message, state: FSMContext):
    if not check_in_admins(message.from_user.id, ADMINS): await message.answer(not_access_message)
    else:
        await state.update_data(title=message.text)
        await state.set_state(TwoWeeksCinemaForm.waiting_for_date_of_start)
        await message.answer("Введите дату начала двух недель (в формате 09.11.2002), это обязательно должен быть понедельник")

@dp.message(TwoWeeksCinemaForm.waiting_for_date_of_start)
async def process_date_of_finish(message: Message, state: FSMContext):
    if not check_in_admins(message.from_user.id, ADMINS): await message.answer(not_access_message)
    else:
        await state.update_data(title=message.text)
        await state.set_state(TwoWeeksCinemaForm.waiting_for_date_of_finish)
        await message.answer("Введите дату финала двух недель (в формате 09.11.2002), это обязательно должно быть воскресенье")

@dp.message(TwoWeeksCinemaForm.waiting_for_date_of_finish)
async def process_cinemas(message: Message, state: FSMContext):
    if not check_in_admins(message.from_user.id, ADMINS): await message.answer(not_access_message)
    else:
        await state.update_data(title=message.text)
        await state.set_state(TwoWeeksCinemaForm.waiting_for_cinemas)
        await message.answer("тут должен стартануть цикл по фильмам")


@dp.message(Command("test_post"))
async def test_post(message: Message):
    if not check_in_admins(message.from_user.id, ADMINS): await message.answer(not_access_message)
    else:
        await bot.send_message(CHANNEL_ID, "Это пост в канале!")
        await message.answer("Я отправил пост в канал Изгойда")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())