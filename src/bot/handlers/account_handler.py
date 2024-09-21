from io import BytesIO
from wave import Error

from aiogram import Router, flags
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup
from src.bot.handlers.commands import Form
from src.anty.actions.add_proxys import add_proxys
from src.anty.actions.accounts import add_accounts, delete_broken_accounts
from src.bot.keyboards.keyboards import custom_kb

accounts_router = Router()
proxy_router = Router()


@accounts_router.message(Form.account)
@flags.authorization(is_authorized=True)
async def add_accounts_tg(message: Message, state: FSMContext):
    if message.text in Form().return_menu():
        data = Form().return_menu()[message.text]
        await state.clear()
        return message.reply(text=data[2] ,reply_markup=ReplyKeyboardMarkup(keyboard=custom_kb(data[1]()), resize_keyboard=True))
    if message.document:
        account_list = await tg_file_to_list(message, binary_to_account)
        await message.answer("Запрос в обработке")
        add_accounts(account_list)
        await message.answer("Аккаунты успешно добавлены")


@proxy_router.message(Form.proxy)
@flags.authorization(is_authorized=True)
async def add_proxy_tg(message: Message, state: FSMContext):
    if message.text in Form().return_menu():
        data = Form().return_menu()[message.text]
        await state.clear()
        return message.reply(text=data[2] ,reply_markup=ReplyKeyboardMarkup(keyboard=custom_kb(data[1]()), resize_keyboard=True))
    if message.document:
        proxy_list = await tg_file_to_list(message, binary_to_proxy)
        if proxy_list:
            await message.answer("Запрос в обработке")
            good_proxies_amount = add_proxys(proxy_list)
            await message.answer(f"{good_proxies_amount}/{len(proxy_list)} прокси успешно добавлено")
        else:
            await message.answer("В файле с прокси ошибка")

async def tg_file_to_list(message, callback) -> list:
    file_id = message.document.file_id
    bot = message.document.bot
    file = await bot.get_file(file_id)
    file_path = file.file_path
    my_object = BytesIO()
    return callback(await bot.download_file(file_path, my_object))


def binary_to_account(bytes_data):
    accounts = []
    decoded_data = bytes_data.read().decode("utf-8")
    for line in str(decoded_data).split("\n"):
        if line:
            data = line.split(":")
            accounts.append({"mail": data[0], "password": data[1], "recovery_mail": data[2], "country": data[3]})
    return accounts


def binary_to_proxy(bytes_data):
    decoded_data = bytes_data.read().decode("utf-8")
    result = []
    for line in str(decoded_data).split("\n"):
        try:
            if line:
                line = line.replace("://", ":")
                data = line.split(":")
                if len(data) > 4:
                    result.append({
                        "scheme": data[0],
                        "host": data[1],
                        "port": data[2],
                        "username": data[3],
                        "password": data[4],
                        "country": data[5]
                    })
                else:
                    result.append({"scheme": data[0], "host": data[1], "port": data[2], "country": data[3]})
        except Exception:
            return False
    return result
