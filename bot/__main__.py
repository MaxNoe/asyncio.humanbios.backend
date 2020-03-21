from aiogram import executor

from . import dp


def main():
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
