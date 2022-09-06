from funcs import *

commands = {
    ('привет', 'здравствуй', 'доброе', 'хай'): play_greetings,
    ('пока', 'свидания', 'стоп', 'завершить'): play_farewell_and_quit,
    ('время', 'времени', 'час'): say_time,
    ('яндекс', 'яндексе'): get_yandex,
    ('погода', 'погоду'): get_weather,
    'no_command': no_command,
}
