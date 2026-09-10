from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
mаin = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="🔍 Старт")],
    [KeyboardButton(text="🎲 Гадание")]
], resize_keyboard = True)