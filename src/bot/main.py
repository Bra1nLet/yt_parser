import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from src.bot.handlers.commands import form_router
from src.bot.handlers.account_handler import accounts_router, proxy_router
from src.bot.handlers.comments_handler import comments_router
from src.bot.middlewares.middleware import AuthorizationMiddleware
from src.config import BOT_TOKEN
from src.bot.handlers.help import help_router
from src.bot.handlers.stat import statistics_rouster
dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    dp.include_router(help_router)
    dp.include_router(form_router)
    dp.include_router(comments_router)
    dp.include_router(accounts_router)
    dp.include_router(proxy_router)
    dp.include_router(statistics_rouster)
    dp.message.middleware(AuthorizationMiddleware())
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
