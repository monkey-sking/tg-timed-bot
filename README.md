# Telegram Timed Bot (GitHub Actions)

<!-- badges:start -->
[![License](https://img.shields.io/github/license/monkey-sking/tg-timed-bot?style=flat-square)](https://github.com/monkey-sking/tg-timed-bot/blob/main/LICENSE) [![Last commit](https://img.shields.io/github/last-commit/monkey-sking/tg-timed-bot?style=flat-square)](https://github.com/monkey-sking/tg-timed-bot/commits/main) [![Python](https://img.shields.io/github/languages/top/monkey-sking/tg-timed-bot?style=flat-square)](https://github.com/monkey-sking/tg-timed-bot/search?l=Python) [![views](https://hits.sh/github.com/monkey-sking/tg-timed-bot.svg?style=flat-square&label=views&color=0e75b6)](https://github.com/monkey-sking/tg-timed-bot)
<!-- badges:end -->

[简体中文](./README.md) | [English](#english)

这是一个利用 GitHub Actions 定时触发运行的 Telegram 机器人项目，专门用于自动签到或发送定时消息。

---

## 🚀 快速上手 (简体中文)

### 1. 本地生成 Session String
为了安全地在 GitHub Actions 中保持登录状态，你需要先在本地生成一个 Session 字符串。

1.  进入项目目录：`cd tg-timed-bot`
2.  安装依赖：`pip install telethon`
3.  运行生成脚本：`python3 gen_session.py`
4.  输入 API ID 和 API HASH (从 [my.telegram.org](https://my.telegram.org) 获取)。
5.  **完整复制**生成的长字符串。

### 2. 配置 GitHub Secrets
在 GitHub 仓库设置中添加以下 Secrets (`Settings` -> `Secrets and variables` -> `Actions`):

- `TG_API_ID`: 你的 Telegram API ID
- `TG_API_HASH`: 你的 Telegram API HASH
- `TG_SESSION_STRING`: 刚才生成的长字符串
- `TG_CHAT_ID`: 接收消息的目标 ID (如频道 ID 或对方机器人 ID)
- `TG_MESSAGE`: (可选) 发送的内容，默认为 `/checkin`

### 3. 设置运行时间
编辑 `.github/workflows/cron_job.yml` 中的 `cron` 表达式：
- 默认 `0 0 * * *` 为北京时间上午 8 点。

---

<a name="english"></a>

## 🚀 Quick Start (English)

### 1. Generate Session String Locally
To maintain login state securely in GitHub Actions, you need to generate a Session string on your local machine first.

1.  Enter project directory: `cd tg-timed-bot`
2.  Install dependencies: `pip install telethon`
3.  Run the generator: `python3 gen_session.py`
4.  Enter your API ID and API HASH (Get them from [my.telegram.org](https://my.telegram.org)).
5.  **Copy the entire** long string generated.

### 2. Configure GitHub Secrets
Add the following Secrets in your repository settings (`Settings` -> `Secrets and variables` -> `Actions`):

- `TG_API_ID`: Your Telegram API ID
- `TG_API_HASH`: Your Telegram API HASH
- `TG_SESSION_STRING`: The long string you just generated
- `TG_CHAT_ID`: The target ID (Channel ID or Bot ID)
- `TG_MESSAGE`: (Optional) Message content, defaults to `/checkin`

### 3. Schedule Time
Edit the `cron` expression in `.github/workflows/cron_job.yml`:
- Default `0 0 * * *` runs at 00:00 UTC (08:00 AM Beijing Time).

## 📄 License
MIT


