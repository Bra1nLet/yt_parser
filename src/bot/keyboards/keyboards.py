from aiogram.types import KeyboardButton


def custom_kb(stats: dict):
    return [[KeyboardButton(text=option)] for option in stats.keys()]


# kb_start = [
#     [KeyboardButton(text="1) Добавить прокси")],
#     [KeyboardButton(text="2) Добавить аккаунты")],
#     [KeyboardButton(text="3) Накрутка")],
#     [KeyboardButton(text="4) Помощь")],
# ]
#
# kb_chose_work = [
#     [KeyboardButton(text="1) YouTube Обычное видео")],
#     [KeyboardButton(text="2) YouTube Shorts")],
#     [KeyboardButton(text="3) YouTube Сообщество")],
#     [KeyboardButton(text="4) Вернуться вернуться в меню")],
# ]
#
#
#
kb_return = [
    [KeyboardButton(text="/cancel")]
]

