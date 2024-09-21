from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

help_proxy_text = """
Поддерживаються протоколы http, socks4, socks5 [без авторизации]
Поддерживается только ipv4
Требуется ввод с файла .txt, один прокси на строку по шаблону:


[Протокол]://[ipv4 адресс]:[порт]:[страна]
[Протокол]://[ipv4 адресс]:[порт]:[логин]:[пароль]:[страна]

Примеры:
socks5://192.168.0.1:8000:switzerland
http://192.168.0.1:8000:username:password:switzerland
"""

help_accounts_text = """
Для ввода аккаунтов с файла, нужно вводить один аккаунт на строку.
Прокси подбирается автоматически (рандомно выбирается один прокси), в зависимости от страны.

Пример:
[почта]:[пароль]:[резервная почта]:[страна]
"""

help_text = """
/help_proxy          | Помощь с добавлением прокси  
/help_accounts       | Помощь с добавлением аккаунтов
/cancel              | Отмена действия
/total_proxy         | Всего прокси
/total_accounts      | Всего аккаунтов
/total_broken        | Получить информацию по нерабочим аккаунтам
/delete_broken       | Удалить нерабочие аккаунты
"""


help_router = Router()


@help_router.message(Command(commands=["help_proxy"]))
async def help_proxy(message: Message) -> None:
    await message.answer(help_proxy_text)


@help_router.message(Command(commands=["help_accounts"]))
async def help_accounts(message: Message) -> None:
    await message.answer(help_accounts_text)


@help_router.message(Command(commands=["help"]))
async def help_(message: Message) -> None:
    await message.answer(help_text)
