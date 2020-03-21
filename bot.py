"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '<hier-einfuegen>'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(regexp='(^meerschweinchen?$|meer|schwein)')
async def cats(message: types.Message):
    breakpoint()
    with open('data/ms.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Hier ist ein meerschweinchen')


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    answer = f'ich habe {message.text} nicht verstanden, \n versuche: meerschweinchen, meer, schwein'
    #await message.answer(answer)
    await message.forward('@humanbios0k')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)