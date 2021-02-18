from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("List of commands: ",
            "/start - start dialog",
            "/help - take help",
            "/history {USD}/{CAD} for {history_days} days - show graphic of rate",
            "/exchange {amount} {USD} to {CAD} - converts to the second currency",
            "/list or /lst - returns list of all available rates",
            "'USD' AND 'CAD' - for example, any currency")
    
    await message.answer("\n".join(text))
