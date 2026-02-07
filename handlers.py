from aiogram import types
from services import check_instagram_status

async def start_handler(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="Проверить Instagram", callback_data="check_instagram")]
        ]
    )
    await message.answer("Привет! Нажми кнопку, чтобы проверить Instagram", reply_markup=keyboard)

async def callback_handler(callback: types.CallbackQuery):
    if callback.data == "check_instagram":
        status_text = await check_instagram_status()
        await callback.message.answer(status_text)
        await callback.answer()  # убираем "часики" на кнопке
