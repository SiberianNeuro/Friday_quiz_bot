from app.database.mailing_sql import get_ids, update_active, get_winners
from app.services.winner_wrapper import winner_wrapper
from loader import dp, bot

from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from app.services.states import LoadTest

import time

async def load_mailing(m: types.Message):
    await m.answer("Понял, начинаем рассылать.\n"
                   "Если передумаешь, напиши <b>/отмена</b>\n\n"
                   "А теперь пришли мне полный текст рассылки."
                   "Вместе с ссылкой на тест")
    await LoadTest.message.set()


async def cancel_handler(m: types.Message, state: FSMContext):
    await state.finish()
    await m.answer("Рассылка остановлена.")

async def start_mailing(m: types.Message, state: FSMContext):
    ids = await get_ids()
    try:
        await m.answer("Держитесь крепче, начинаем рассылку.\n\n"
                       "Остановить процесс нельзя 😈")
        for id in ids:
            bot.send_message(id[0], m.text)
            time.sleep(0.1)
    except ids is None:
        await m.answer("Не вышло достать список пользователей. Караул.")
    finally:
        await m.answer("Рассылка закончена.")
        await state.finish()


async def get_losers(m: types.Message):
    await m.answer("Скопируй из таблички победителей колонку 'ID' и пришли мне,"
                   "а дальше я сам.\n\n"
                   "Если передумаешь, напиши <b>/отмена</b>")


async def kick_losers(m: types.Message):
    winners = tuple(map(int, m.text.split('\n')))
    await update_active(winners)
    await m.answer(f"Готово. Текущий список победителей:\n\n"
                   f"{winner_wrapper()}")


def register_mailing_handlers(dp: Dispatcher):
    dp.register_message_handler(load_mailing, commands=['рассылка'], is_admin=True)
    dp.register_message_handler(cancel_handler, commands=['отмена'], state="*")
    dp.register_message_handler(start_mailing, state=LoadTest.message)
    dp.register_message_handler(get_losers, commands=['победители'])