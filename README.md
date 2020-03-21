# asyncio.humanbios.backend
The humanbios bios python backend with asyncio + aiogramm

We use aiogramm for the bot related things: https://github.com/aiogram/aiogram/blob/dev-2.x/README.md

Use telegrams botfather to generate an API token, see https://t.me/botfather


## Getting started

This is a python project using [`poetry`](https://python-poetry.org/docs/basic-usage).

You'll need python ≥ 3.6.

1. Get poetry:
    ```
    $ pip install [--user] poetry
    ```

1. Copy the env-template and fill in the config
    ```
    $ cp env-template .env
    ```

1. Install dependencies
    ```
    $ poetry install
    ```

1. Run database migrations
    ```
    $ poetry run python -m bot
    ```

1. Run the unit tests

    ```
    $ poetry run python -m pytest
    ```
