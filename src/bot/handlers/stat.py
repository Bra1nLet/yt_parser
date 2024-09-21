from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery
from src.models.proxy import proxy_countries, proxy_quantity
from src.models.accounts import accounts_countries, accounts_quantity

statistics_rouster = Router()


@statistics_rouster.message(Command("total_proxy"))
async def total_proxy(query: CallbackQuery):
    countries = proxy_countries()
    message = "Всего прокси: " + str(proxy_quantity()) + "\n" + f"В {len(countries)} странах:"
    for key in countries:
        message += "\n" + key + "| " + str(proxy_quantity(key))
    await query.answer(message)


@statistics_rouster.message(Command("total_accounts"))
async def total_accounts(query: CallbackQuery):
    quantity = accounts_quantity(is_broken=False)
    quantity_total = accounts_quantity()
    countries = accounts_countries()
    msg = f"Всего рабочих аккаунтов:  {quantity}/{quantity_total}  \nВ {len(countries)} странах:"
    for country in countries:
        msg += f"\n{country}| {accounts_quantity(country, False)}/{accounts_quantity(country)}"
    await query.answer(msg)


@statistics_rouster.message(Command("total_broken"))
async def total_accounts(query: CallbackQuery):
    quantity_total = accounts_quantity()
    broken_accounts = accounts_quantity(is_broken=True)
    countries = accounts_countries()
    msg = f"Всего не рабочих аккаунтов: {broken_accounts}/{quantity_total}"
    msg += f"\nНе рабочих аккаунтов по странам:"
    for country in countries:
        msg += f"\n{country}| {accounts_quantity(country, True)}/{accounts_quantity(country)}"
    await query.answer(msg)
