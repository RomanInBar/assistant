# assistant
## Описание
Бот-ассистент с голосовым управлением.
По умолчанию стоит женский голос, распознаёт русскую речь, но так же можно опереключить на английский язык и поменять речевые настройки.
В файле `assistant.py`, на 84 строке, вариант печатного обращения к боту. Закоментируйте 83 строку и раскоментируйте 84.
 - Отвечает на приветствие
 - Предоставляет по запросу информацию о погоде
 - Отправляет запросы в браузер(яндекс)
 - Подскажет который час
 - При прощании завершает программу.

## Установка
Чтобы скачать репозиторий, пропишите в терминале `git clone https://github.com/RomanInBar/assistant.git`.  
 Для работы функции погоды, необходимо получить токен на сайте `OpenWeather`, получить его можно в личном кабинете после регистрации, и записать его в `.env` файл, предварительно создав его, в переменную `WEATHER_TOKEN`. 
 Все логи будут записываться в файл `assistant.log`. 
 Не забудьте установить виртуальное окружение(командой `python -m venv env`) и активировать его(`env/bin/activate`(если у вас windows, команда выглядит так - `env/Scripts/activate`)), после чего в терминале должно появится `(env)`. Если всё так, в терминале, введите команду `pip install -r requirements.txt`, она установит все необходимые зависимости в виртуальное окружение.

