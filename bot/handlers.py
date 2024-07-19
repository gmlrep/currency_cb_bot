from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from bot.redis_client import get_all_currencies, get_currency

router = Router()


@router.message(Command('exchange'))
async def exchange_command(message: Message, command: CommandObject):
    cmd_args = command.args.split(' ')
    try:
        data = await get_currency(valute_code=cmd_args[0])
        cur_value = float(cmd_args[2]) * float(data['value'])
        print(cur_value)
        await message.answer(text=f"{cmd_args[2]} {cmd_args[0]} стоит {round(cur_value, 3)} RUB")
    except ValueError:
        await message.answer(text='Неверный формат аргументов команды.\nПример: /exchange AUD RUB 10')


@router.message(Command('rates'))
async def get_rates(message: Message):
    data = await get_all_currencies()
    msg = "Курсы валют:\n"
    for cur in data:
        msg += f"{data[cur]['name']}: 1 {cur} - {data[cur]['value']} RUB\n"
    await message.answer(text=msg)
