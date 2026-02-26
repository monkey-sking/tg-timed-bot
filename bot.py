from telethon import TelegramClient, events
import os
import asyncio
import sys

# 从环境变量获取敏感信息
API_ID = os.getenv('TG_API_ID')
API_HASH = os.getenv('TG_API_HASH')
SESSION_STRING = os.getenv('TG_SESSION_STRING')
CHAT_ID = os.getenv('TG_CHAT_ID')  # 可以是用户名如 @mychannel 或 ID -100...
MESSAGE = os.getenv('TG_MESSAGE', 'Hello from GitHub Actions!')

async def main():
    if not API_ID or not API_HASH or not SESSION_STRING:
        print("Error: Required environment variables are missing.")
        sys.exit(1)

    # 使用 Session String 登录，避免在 GitHub Actions 中交互输入验证码
    from telethon.sessions import StringSession
    client = TelegramClient(StringSession(SESSION_STRING), int(API_ID), API_HASH)
    
    await client.connect()
    
    if not await client.is_user_authorized():
        print("Error: The provided session string is invalid or expired.")
        sys.exit(1)

    # 尝试解析 CHAT_ID
    target = CHAT_ID
    if CHAT_ID.startswith('-') or CHAT_ID.isdigit():
        try:
            target = int(CHAT_ID)
            print(f"Parsed CHAT_ID as integer: {target}")
        except ValueError:
            pass

    print(f"Attempting to send message to {target}...")
    try:
        # 第一步：尝试直接获取或从对话列表刷新
        try:
            entity = await client.get_input_entity(target)
        except Exception:
            print("Entity not found in cache, fetching dialogue list...")
            await client.get_dialogs()
            entity = await client.get_input_entity(target)
            
        await client.send_message(entity, MESSAGE)
        print("Message sent successfully!")
        
    except Exception as e:
        print(f"Failed to send message: {e}")
        print("\n--- 诊断与建议 ---")
        if "entity" in str(e).lower():
            print("1. 如果目标是 Bot，请先在 Telegram 里给它发个消息。")
            print("2. 确保 CHAT_ID 正确。如果是给机器人发消息，请确认填入的是『你的个人用户 ID』还是『对方机器人的 ID』。")
            print("3. 如果是给频道/群组发消息，请确保已加入该频道/群组。")
        sys.exit(1)
    finally:
        await client.disconnect()



if __name__ == '__main__':
    asyncio.run(main())
