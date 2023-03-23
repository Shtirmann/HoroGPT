import openai
from aiogram import Bot
import asyncio
from Data.config import *
from Data.prompt import GeneratePrompt

openai.api_key = APIKEY


async def PostMessage():
    bot = Bot(token=BOTTOKEN)
    prompt = GeneratePrompt()
    completion = openai.Completion.create(engine=ENGINE,
                                          prompt=prompt[0],
                                          temperature=prompt[1],
                                          max_tokens=1024)
    await bot.send_message(text=completion["choices"][0]["text"],
                           chat_id=-1001806378959,
                           parse_mode='HTML')
    # print(prompt[1])
    await asyncio.sleep(86400)  # 24 часа в секундах
    await bot.close()


while True:
    asyncio.get_event_loop().run_until_complete(PostMessage())
