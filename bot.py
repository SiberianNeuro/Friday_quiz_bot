import logging

from aiogram.utils import executor

from loader import dp



async def on_startup(dispatcher):
    logging.basicConfig(
        format=u"%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s",
        level=logging.INFO
    )




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)