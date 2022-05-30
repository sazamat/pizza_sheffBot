from aiogram.utils import executor
from create_bot import dp
from database import sqlite


async def on_startup(_):
    print('Бот вышел в онлайн')
    sqlite.sql_start()


from handlers import client, admin, general

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
general.register_handlers_general(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
