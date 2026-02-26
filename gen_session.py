from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio

async def generate():
    print("Telethon Session 字符串生成器")
    api_id = input("输入 API ID: ")
    api_hash = input("输入 API HASH: ")
    
    async with TelegramClient(StringSession(), int(api_id), api_hash) as client:
        print("\n--- 你的 SESSION STRING 如下 ---")
        print(client.session.save())
        print("--------------------------------")
        print("请复制上面这行长字符串，并存入 GitHub Secrets (命名为 TG_SESSION_STRING)。")

if __name__ == '__main__':
    asyncio.run(generate())
