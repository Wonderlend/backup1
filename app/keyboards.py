from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton

from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


async def are_you_ready_button():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="да", callback_data="go_to_day_1"))
    keyboard.add(InlineKeyboardButton(text="нет", callback_data="user_not_ready"))
    return keyboard.adjust(2).as_markup()


# async def keybodard_for_day():
#     keyboard = InlineKeyboardBuilder()
#     keyboard.add(InlineKeyboardButton(text="Некст дей йоу", callback_data="plus_day"))
#     return keyboard.adjust(2).as_markup()


# connect_to_curator = ReplyKeyboardMarkup(
#     [[KeyboardButton(text="Связь с куратором")]], resize_keyboard=True
# ) 

