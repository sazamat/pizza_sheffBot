from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Кнопки клавиатуры для админа
button_load = KeyboardButton('/Загрузить')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load)