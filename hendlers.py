from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from generation import *

router = Router()

class Gen(StatesGroup):
    wait = State()


@router.message(CommandStart())
async def main(message: Message):
    await message.answer("Привет! Я твой персональный помощник в учебном процессе. Ты можешь задать вопрос по интересующей теме!")

@router.message(Gen.wait)
async def anti_flood(message: Message):
    await message.answer("Дождитесь окончание генерации прошлого процесса!")

@router.message()
async def request_processing(message: Message, state: FSMContext):
    await state.set_state(Gen.wait)

    responce = await generate(message.text)
    await message.reply(responce)
    await state.clear()

