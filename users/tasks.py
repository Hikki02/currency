import requests

from telegramm_bot.data.config import BOT_TOKEN
from telegramm_bot.data.services import get_currency
from users.models import TelegramUser
from celery import shared_task


@shared_task
def send_a_currency_notification() -> None:
    response = get_currency()
    users = TelegramUser.objects.all()
    for i in users:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={i.t_id}&text={response}"
        requests.get(url)
    return
