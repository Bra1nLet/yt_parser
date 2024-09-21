from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup
from src.bot.keyboards.keyboards import kb_return
from src.bot.handlers.account_handler import Form, tg_file_to_list
from src.models.accounts import accounts_countries

comments_router = Router()


@comments_router.message(Form.comments)
async def write_comments(message: Message, state: FSMContext):
    comments = await tg_file_to_list(message, binary_to_comments)
    await state.update_data(total=len(comments))
    await state.update_data(comments=comments)
    await state.set_state(Form.url)
    text = "Скиньте ссылку на видео: \n"
    await message.answer(text, reply_markup=ReplyKeyboardMarkup(keyboard=kb_return, resize_keyboard=True))


def binary_to_comments(bytes_data):
    comments = []
    decoded_data = bytes_data.read().decode("utf-8")
    for line in str(decoded_data).split("\n"):
        if line:
            comments.append(line)
    return comments
