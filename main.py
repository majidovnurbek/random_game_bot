import asyncio
import logging
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from config import Token
from button import *

import random

TOKEN = Token

router = Router()
dp = Dispatcher()
dp.include_router(router)


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("salom bizni o'yin botimizga xush kelibsiz",
                         reply_markup=catalog)


ran = random.randint(1, 10)


@router.callback_query(F.data == "a")
async def game(call: CallbackQuery):
    await call.message.answer("1 da n 10 gacha bo'lgan xohlagan bitta raqam kiriting")

    @dp.message()
    async def game(message: Message):
        text = message.text
        if int(text) == ran:
            await message.answer("✅")
        else:
            await message.answer("topolmadingiz ‼️‼️")


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
