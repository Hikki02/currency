import asyncio
import logging
import random
import time

from aiogram import Dispatcher

from telegramm_bot.data.config import ADMINS, BOT_TOKEN


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)
