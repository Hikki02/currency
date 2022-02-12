from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from asgiref.sync import sync_to_async

from telegramm_bot.data.services import get_currency
from telegramm_bot.loader import dp, bot
from users.models import TelegramUser


@sync_to_async
def added_user(name: str, pk: str) -> None:
    TelegramUser.objects.get_or_create(username=name, t_id=pk)
    return


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    response = get_currency()
    user = message.from_user
    await added_user(user.username, user.id)
    await message.answer(f"Привет, {message.from_user.full_name}🤗 \n{response}")
