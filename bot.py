import json
import datetime
import asyncio
from aiogram import Bot, Dispatcher

# Replace with your actual bot token and channel ID
BOT_TOKEN = '8135912668:AAFdJoEZptfueGb2OvDSTSf8XlpEuWqXBUI'
CHANNEL_ID = '@fazliddins_life'  # or '-100xxxxxxxxxx'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def send_daily_post():
    # Load content
    with open("content.json", "r", encoding="utf-8") as f:
        content = json.load(f)

    # Get today's day
    today = datetime.datetime.now().strftime("%A")

    # Get message for today
    message = content.get(today)
    if message:
        await bot.send_message(chat_id=CHANNEL_ID, text=message)
    else:
        print("No post for today.")

async def main():
    await send_daily_post()

if __name__ == "__main__":
    asyncio.run(main())
