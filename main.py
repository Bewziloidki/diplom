# main.py

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from handlers import start_handler, callback_handler

# 1️⃣ Токен бота
API_TOKEN = "8559228120:AAEC5-ZJt4q-nRad7__r4F2ieNo01IGWapk"

# 2️⃣ Создаем объекты бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# 3️⃣ Регистрируем обработчик команды /start
dp.message.register(start_handler, Command(commands=["start"]))

# 4️⃣ Регистрируем обработчик нажатий кнопок
dp.callback_query.register(callback_handler)

# 5️⃣ Асинхронный запуск бота
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
