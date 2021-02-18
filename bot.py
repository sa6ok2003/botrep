from aiogram import Bot, types, Dispatcher, executor

TOKEN = '1686424554:AAEUySebIA2fuA94jzhb8SQFfQbBSflvJp0'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome(message: types.message):
    await bot.send_message(message.chat.id, 'Бот 1 Запущен')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)