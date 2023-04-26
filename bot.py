from checkWord import checkWord
from aiogram import Bot,Dispatcher,executor,types
API_TOKEN='6061272356:AAHy1KSLUGJJSn9BQykLtIpsswjJ5rT_B6A'
bot=Bot(token=API_TOKEN)
db=Dispatcher(bot)


@db.message_handler(commands='start')
async def send_welcome(message:types.Message):
    await message.reply("Imlo botiga xush kelibsiz")

@db.message_handler(command='help')
async def send_help(message:types.Message):
    await message.answer('Bironta so\'z kiriting.Xatosini tekshiramiz')

@db.message_handler()
async def checkImlo(message:types.Message):
    word=message.text
    result=checkWord(word)
    if result['available']:
        response=f'&&{word.capitalize()}'
    else:
        response=f'x{word.capitalize()}\n'
        for text in result['matches']:
            response+=f'&{text.capitalize()}\n'
    await message.answer(response)


if __name__=='__main__':
    executor.start_polling(db,skip_updates=True)
