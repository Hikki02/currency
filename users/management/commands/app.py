from aiogram.types import BotCommand
from django.core.management import BaseCommand
from telegramm_bot import filters, middlewares, utils
from telegramm_bot.loader import bot


async def set_commands(bot):
    commands = [
        BotCommand(command="/start", description="начать"),
        BotCommand(command="/help", description="помощь"),
    ]
    await bot.set_my_commands(commands)


async def on_startup(dp):
    # filters.setup(dp)
    # middlewares.setup(dp)

    await set_commands(bot=bot)
    await utils.notify_admins.on_startup_notify(dp)


class Command(BaseCommand):
    help = 'Telegramm Bot'

    def handle(self, *args, **options):
        from aiogram import executor
        from telegramm_bot.handlers import dp
        executor.start_polling(dp, on_startup=on_startup)
