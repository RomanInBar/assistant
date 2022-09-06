import logging

import pyttsx3
import speech_recognition

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler('assistant.log', 'w', 'utf-8')],
    format='%(asctime)s %(levelname)s %(name)s: %(message)s'
)
logger = logging.getLogger(__name__)


class VoiceAssistant:
    """Основные данные бота."""
    name: str
    sex: str
    speech_language: str
    recordition_language: str


def setup_assistant_vioce():
    """Выборка языка и голоса."""
    voices = ttsEngine.getProperty('voices')
    if assistant.speech_language == 'en':
        assistant.recordition_language = 'en-US'
        if assistant.sex == 'female':
            ttsEngine.setProperty('voice', voices[1].id)
        else:
            ttsEngine.setProperty('voice', voices[2].id)
    else:
        assistant.recordition_language = 'ru-RU'
        ttsEngine.setProperty('voice', voices[0].id)


def record_and_recognize_audio(*args: tuple):
    """Запись и распознование речи."""
    with microphone:
        recognized_data = ''
        recognizer.adjust_for_ambient_noise(microphone, duration=2)
        try:
            print('Слушаю...')
            audio = recognizer.listen(microphone, 5, 5)
        except speech_recognition.WaitTimeoutError:
            print('Проверьте свой микрофон')
            return
        try:
            print('Распознаю...')
            recognized_data = recognizer.recognize_google(
                audio, language='ru').lower()
        except speech_recognition.UnknownValueError:
            pass
        except speech_recognition.RequestError:
            print('Проверьте подключение к интернету')
        return recognized_data


def execute_commands(command_name: str, *args: list) -> bool:
    """Проверка на наличие команды."""
    for key in commands.keys():
        if command_name in key:
            commands[key](*args)
            return True


def make_preparation():
    """Установка основных переменных."""
    global assistant, recognizer, microphone, ttsEngine
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()
    assistant = VoiceAssistant()
    ttsEngine = pyttsx3.init()
    assistant.name = 'Lora'
    assistant.sex = 'female'
    assistant.speech_language = 'ru'
    setup_assistant_vioce()


if __name__ == '__main__':
    from config import commands
    make_preparation()
    while True:
        voice_input = record_and_recognize_audio().split()
        # voice_input = input('Введите запрос: ').split()
        for index, word in enumerate(voice_input):
            if execute_commands(word, voice_input[index+1:]):
                break
        else:
            commands['no_command']()
