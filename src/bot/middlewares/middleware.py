import logging
from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from aiogram.types import Message, TelegramObject
from src.config import ADMIN_TG_IDS

logger = logging.getLogger(__name__)


class AuthorizationMiddleware(BaseMiddleware):
    """
    Helps to check if user is authorized to use the bot
    """

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        if not isinstance(event, Message):
            return await handler(event, data)

        authorization = get_flag(data, "authorization")
        print("Authorization: ", authorization)
        if authorization is not None:
            if authorization["is_authorized"]:
                if event.from_user.id in ADMIN_TG_IDS:
                    return await handler(event, data)
                else:
                    return None
        else:
            return await handler(event, data)
