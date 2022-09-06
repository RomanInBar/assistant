import logging
import os
import webbrowser
from datetime import datetime
from typing import Union

import dotenv
import pyttsx3
import requests

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler('assistant.log', 'w', 'utf-8')],
    format='%(asctime)s %(levelname)s %(name)s: %(message)s'
)
logger = logging.getLogger(__name__)


dotenv.load_dotenv()
ttsEngine = pyttsx3.init()


def play_greetings(*args: tuple):
    """Функция команды приветствия."""
    play_voices_assistant_speech('Привет, чем я могу помочь?')


def play_farewell_and_quit(*args: tuple):
    """Функция команды прощания и завершение программы."""
    play_voices_assistant_speech('Пока пока.')
    quit()


def say_time(*args: tuple):
    """Функция команды время."""
    time = datetime.now().strftime('%H:%M')
    play_voices_assistant_speech(f'Текущее время {time}')


def get_yandex(*args: tuple):
    """Функция команды поиск в яндексе."""
    search = ' '.join(args[0])
    url = f'https://yandex.ru/search/?text={search}'
    logger.info(url)
    webbrowser.get().open(url)


def temperature(val: Union[int, float]) -> str:
    """Функция определяет окончание слова для температуры."""
    if val >= 0:
        symbol = 'тепла'
    elif val < 0:
        symbol = 'мороза'
    ex = [11, 12, 13, 14]
    if val % 10 == 1 and val not in ex:
        return f'градус {symbol}'
    if val % 10 in [2, 3, 4] and val not in ex:
        return f'градуса {symbol}'
    return f'градусов {symbol}'


def wind_speed(speed: Union[int, float]) -> str:
    """Функция определяет окончание слова для скорости ветра."""
    ex = [11, 12, 13, 14]
    if speed % 10 == 1 and speed not in ex:
        return 'метр в секунду'
    if speed % 10 in [2, 3, 4] and speed not in ex:
        return f'метра в секунду'
    return f'метров в секунду'


def get_weather(*args: tuple):
    """Функция для команды погода"""
    data = requests.get(
        "http://api.openweathermap.org/data/2.5/weather",
        params={
            'q': 'Moscow',
            'lang': 'ru',
            'units': 'metric',
            'APPID': os.getenv('WEATHER_TOKEN')
        }
    ).json()
    weather = data['weather'][0]['description']
    temp = int(data['main']['temp'])
    wind = data['wind']['speed']
    text = f'В Москве {weather}, {temp} {temperature(temp)}, скорость ветра - {wind} {wind_speed(wind)}'
    play_voices_assistant_speech(text)


def no_command(*args: tuple):
    """Функция включается при невозможности разпознать команду."""
    play_voices_assistant_speech('Команда не распознана.')


def play_voices_assistant_speech(text):
    """Функция конвертации текста в речь, запуск речи."""
    ttsEngine.say(str(text))
    ttsEngine.runAndWait()
