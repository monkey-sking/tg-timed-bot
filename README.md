# Telegram 定时消息机器人 (GitHub Actions)

这是一个利用 GitHub Actions 定时触发运行的 Telegram 机器人项目。

## 快速上手

### 1. 本地生成 Session String
为了安全地在 GitHub Actions 中保持登录状态，你需要先在本地生成一个 Session 字符串。

1. 进入项目目录：`cd tg-timed-bot`
2. 安装依赖：`pip install telethon`
3. 运行生成脚本：`python gen_session.py`
4. 按照提示输入从 [my.telegram.org](https://my.telegram.org) 获取的 `API_ID` 和 `API_HASH`。
5. 复制生成的 **长字符串**。

### 2. 配置 GitHub Secrets
将项目推送到 GitHub 的 **Private (私有)** 仓库后，在仓库设置中添加以下 Secrets (`Settings` -> `Secrets and variables` -> `Actions`):

- `TG_API_ID`: 你的 Telegram API ID
- `TG_API_HASH`: 你的 Telegram API HASH
- `TG_SESSION_STRING`: 刚才生成的长字符串
- `TG_CHAT_ID`: 接收消息的目标（例如 `@your_channel` 或数字 ID）

### 3. 设置定时时间
编辑 `.github/workflows/cron_job.yml` 中的 `cron` 表达式：
- 默认 `0 0 * * *` 为 UTC 时间 0 点（北京时间上午 8 点）。

## 文件说明
- `bot.py`: 核心发送逻辑。
- `gen_session.py`: 登录验证工具。
- `.github/workflows/cron_job.yml`: GitHub 自动化配置。
