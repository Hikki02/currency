import requests

from telegramm_bot.data.config import url


def get_currency():
    response = requests.get(url=url)
    if response.status_code != 200:
        return
    data = response.json()
    data = data['Valute']['USD']
    response = f"1 {data['CharCode']} = {data['Value']} руб"
    return response
