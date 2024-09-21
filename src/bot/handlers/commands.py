from aiogram import Router, F, flags
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup
from src.anty.actions.accounts import delete_broken_accounts
from src.bot.keyboards.keyboards import custom_kb, kb_return
from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.state import State, StatesGroup
from src.models.accounts import accounts_countries, get_good_accounts, Account, accounts_quantity

form_router = Router()


class Form(StatesGroup):
    delete_account = State()
    work = State()

    community = State()
    shorts = State()
    video = State()

    action = State()
    country = State()
    total = State()
    url = State()

    proxy = State()
    account = State()

    likes = State()
    comments = State()
    like_comments = State()
    reply_comments = State()
    votes = State()

    def videos_states(self) -> dict:
        return {
            "1) Накрутка лайков": (self.country, self.country_states, "Выберите страну", "likes"),
            "2) Накрутка коментариев": (self.country, self.country_states, "Выберите страну", "comments"),
            "3) Накрутка лайков на коментарий": (self.country, self.country_states, "Выберите страну", "like_comment"),
            "4) Накрутка ответов под коментарий": (self.country, self.country_states, "Выберите страну", "reply_comments"),
            "5) Вернуться в меню": (None, None, "Выберите действие")
        }


    def community_states(self) -> dict:
        return {
            "1) Накрутка лайков": (self.country, self.country_states, "Выберите страну", "likes"),
            "2) Накрутка коментариев": (self.country, self.country_states, "Выберите страну", "comments"),
            "3) Накрутка лайков на коментарий": (self.country, self.country_states, "Выберите страну", "like_comment"),
            "4) Накрутка ответов под коментарий": (self.country, self.country_states, "Выберите страну", "reply_comments"),
            "5) Накрутка голосов в опросах": (self.country, self.country_states, "Выберите страну", "reply_votes"),
            "6) Вернуться в меню": (None, None, "Выберите действие")
        }

    def country_states(self):
        return {f"{country}|{accounts_quantity(country=country, is_broken=False)}": (self.url, None, "Отрваьте ссылку на видео/сообщество") for country in accounts_countries()}

    def start_states(self) -> dict:
        return {
            "1) Добавить прокси":  (self.proxy, self.return_menu, "Скиньте файл с прокси"),
            "2) Добавить аккаунты": (self.account, self.return_menu, "Скиньте файл с аккаунтами"),
            "3) Накрутка": (self.work, self.working_states, "Выберите объект накрутки"),
            "4) Помощь": (None, self.start_states, "Пропишите /help")
        }

    def working_states(self):
        return {
            "1) YouTube Обычное видео": (self.video, self.videos_states, "Выберите действие", "video"),
            "2) YouTube Shorts": (self.shorts, self.videos_states, "Выберите действие", "shorts"),
            "3) YouTube Сообщество": (self.community, self.community_states,"Выберите действие", "community"),
            "4) Вернуться вернуться в меню": (None, self.start_states, "Выберите действие")
        }

    def return_menu(self):
        return {
            "1) Вернуться назад в меню": (None, self.start_states, "Выберите действие")
        }

    def get_action_by_state(self, state):
        return {
            self.video.state: self.videos_states,
            self.shorts.state: self.videos_states,
            self.community.state: self.community_states,
        }[state]

@form_router.message(CommandStart())
@flags.authorization(is_authorized=True)
async def start(message: Message) -> None:
    await message.reply(text="Выберите действие",
                        reply_markup=ReplyKeyboardMarkup(keyboard=custom_kb(Form().start_states()), resize_keyboard=True))

@form_router.message(StateFilter(None))
@flags.authorization(is_authorized=True)
async def start_handler(message: Message, state: FSMContext) -> None:
    if not await state.get_data():
        if message.text in Form().start_states().keys():
            data = Form().start_states()[message.text]
            if data[0]:
                await state.set_state(data[0])
            else:
                await state.clear()
            if data[1]:
                await message.reply(text=data[2] ,reply_markup=ReplyKeyboardMarkup(keyboard=custom_kb(data[1]()), resize_keyboard=True))
            else:
                await message.reply(text=data[2], reply_markup=ReplyKeyboardMarkup(keyboard=kb_return, resize_keyboard=True))
        else:
            await message.reply("got 404")



@form_router.message(Form.work)
@flags.authorization(is_authorized=True)
async def chose_type_handler(message: Message, state: FSMContext) -> None:
    if not await state.get_data():
        if message.text in Form().working_states().keys():
            data = Form().working_states()[message.text]
            if data[0]:
                await state.set_data({"type": data[3]})
                await state.set_state(data[0])
            else:
                await state.clear()
            await message.reply(text=data[2] ,reply_markup=ReplyKeyboardMarkup(keyboard=custom_kb(data[1]()), resize_keyboard=True))
        else:
            await message.reply("got 404")


@form_router.message(Form.video)
@form_router.message(Form.community)
@form_router.message(Form.shorts)
@flags.authorization(is_authorized=True)
async def chose_action_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if message.text in Form().get_action_by_state(current_state)().keys():
        data = Form().get_action_by_state(current_state)()[message.text]
        if data[0]:
            await state.update_data({"action": data[3]})
            await state.set_state(data[0])
        else:
            await state.clear()
        if data[1]:
            await message.reply(text=data[2] ,reply_markup=ReplyKeyboardMarkup(keyboard=custom_kb(data[1]()), resize_keyboard=True))
        else:
            await message.reply(text=data[2] ,reply_markup=ReplyKeyboardMarkup(keyboard=custom_kb(Form().start_states()), resize_keyboard=True))
    else:
        await message.reply("got 404")


@form_router.message(Command("delete_broken"))
@flags.authorization(is_authorized=True)
async def delete_broken_accounts_tg(message: Message):
    await message.answer("Запрос в обработке")
    delete_broken_accounts()
    await message.answer("Поломанные аккаунты успешно удалены")


@form_router.message(Command("cancel"))
@flags.authorization(is_authorized=True)
async def cancel_handler(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        "Выберите действие",
        reply_markup=ReplyKeyboardMarkup(keyboard=custom_kb(Form().start_states()), resize_keyboard=True),
    )


@flags.authorization(is_authorized=True)
async def chose_action(message: Message, state: FSMContext):
    if message.text in Form().working_states().keys():
        data = Form().working_states()[message.text]
        await state.set_state(data[0])
        await message.answer(data[2], reply_markup=data[1])


@form_router.message(Form.action)
@flags.authorization(is_authorized=True)
async def chose_action(message: Message, state: FSMContext):
    if message.text in Form().working_states().keys():
        data = Form().working_states()[message.text]
        await state.set_state(data[0])
        await message.answer(data[2], reply_markup=data[1])


@form_router.message(Form.country)
@flags.authorization(is_authorized=True)
async def country(message: Message, state: FSMContext):
    await state.update_data(country=message.text.split("|")[0])
    if message.text in Form().return_menu().keys():
        await state.clear()
        await message.answer("Скиньте ссылку на сообщество",
                             reply_markup=ReplyKeyboardMarkup(keyboard=kb_return, resize_keyboard=True))

    if (await state.get_data())["action"] in ["reply_comments", "comments"]:
        await state.set_state(Form.comments)
        await message.answer("Добавьте файл с комментариями:",
                             reply_markup=ReplyKeyboardMarkup(keyboard=kb_return, resize_keyboard=True))
    elif (await state.get_data())["action"] == "reply_votes":
        await state.set_state(Form.votes)
        await message.answer("Отправьте ответы на вопрос в формате 'опция-колличество голосов, на одну опцию, одна строка':\n1-4\n3-6\n",
                             reply_markup=ReplyKeyboardMarkup(keyboard=kb_return, resize_keyboard=True))
    elif (await state.get_data())["action"] in ["likes", "like_comment"]:
        await state.set_state(Form.total)
        await message.answer("Укажите колличество лайков", reply_markup=ReplyKeyboardMarkup(keyboard=kb_return, resize_keyboard=True))


@form_router.message(Form.total)
@flags.authorization(is_authorized=True)
async def country(message: Message, state: FSMContext):
    await state.update_data(total=int(message.text))
    await state.set_state(Form.url)
    await message.answer("Скиньте ссылку на видео", reply_markup=ReplyKeyboardMarkup(keyboard=kb_return, resize_keyboard=True))

@form_router.message(Form.votes)
@flags.authorization(is_authorized=True)
async def vote(message: Message, state: FSMContext):
    lines = message.text.split("\n")
    votes = []
    try:
        for line in lines:
            line = line.split("-")
            votes += [line[0] for _ in range(int(line[1]))]
        await state.update_data(total=len(votes))
        await state.update_data(votes=votes)
        await state.set_state(Form.url)
        print(votes)
        await message.answer("Скиньте ссылку на опрос", reply_markup=ReplyKeyboardMarkup(keyboard=kb_return, resize_keyboard=True))
    except:
        await message.answer("Неправильный формат")

@form_router.message(Form.url)
@flags.authorization(is_authorized=True)
async def final(message: Message, state: FSMContext):
    data = (await state.get_data())
    type_ = data["type"]
    action = data["action"]
    amount = data["total"]
    country = data["country"]
    print(data)
    comments = []
    votes = []
    if "comments" in data.keys():
        comments = data["comments"]

    if "votes" in data.keys():
        votes = data["votes"]

    url = message.text
    accounts = get_good_accounts(country=country, quantity=amount)
    result = []
    await message.answer(f"Запрос в обработке ({action})",
                         reply_markup=ReplyKeyboardMarkup(keyboard=custom_kb(Form().start_states()), resize_keyboard=True))
    await state.clear()
    comment_id = 0
    vote_id = 0
    for account in accounts:
        actions = {
            "video|likes": (account.video_like, {"url": url}),
            "video|comments": (account.video_comment, {"url": url, "comments": comments}),
            "video|like_comment": (account.video_comment_like, {"url": url}),
            "video|reply_comments": (account.video_comment_reply, {"url": url, "comments": comments}),

            "shorts|likes": (account.shorts_like, {"url": url}),
            "shorts|comments": (account.video_comment, {"url": url, "comments": comments}),
            "shorts|like_comment": (account.video_comment_like, {"url": url}),
            "shorts|reply_comments": (account.video_comment_reply, {"url": url, "comments": comments}),

            "community|likes": (account.community_like, {"url": url}),
            "community|comments": (account.community_comment, {"url": url, "comments": comments}),
            "community|like_comment": (account.community_comment_like, {"url": url}),
            "community|reply_comments": (account.community_comment_reply, {"url": url, "comments": comments}),
            "community|reply_votes": (account.reply_vote, {"url": url, "votes": votes}),
        }[f"{type_}|{action}"]

        if action in ["likes", "like_comment"]:
            result.append(actions[0](**actions[1]))
        elif action in ["comments", "reply_comments"]:
            result.append(actions[0](**{"url":actions[1]["url"], "comment":actions[1]["comments"][comment_id]}))
            comment_id += 1
        elif action == "reply_votes":
            result.append(actions[0](**{"url": actions[1]["url"], "option_id": actions[1]["votes"][vote_id]}))
            vote_id += 1

    msg = "Запрос обработан"
    msg += (f"\n{result.count(False)} Аккаунтов поломалось."
            f"\n{result.count(True)} Аккаунтов прошло.")
    await message.answer(msg)

async def validate_total(message: Message):
    if message.text.isdigit():
        if 0 < int(message.text) <= accounts_quantity():
            return True
        await message.answer("Число аккаунтов слишком большое(у вас нет стольки аккаунтов) или введено 0")
    else:
        await message.answer("Нужно ввести положительное число")
