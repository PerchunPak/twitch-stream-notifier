# twitch-stream-notifier

[![Support Ukraine](https://badgen.net/badge/support/UKRAINE/?color=0057B8&labelColor=FFD700)](https://www.gov.uk/government/news/ukraine-what-you-can-do-to-help)

[![Build Status](https://github.com/PerchunPak/twitch-stream-notifier/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/PerchunPak/twitch-stream-notifier/actions?query=workflow%3Atest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python support versions badge](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/downloads/)

Script to send notification when someone starts streaming on Twitch.

## How to use

```bash
docker run -d \
  -v /path/to/data:/app/data \
  --restart=unless-stopped \
  perchunpak/twitch-stream-notifier:latest
```

Then go to data folder and edit `config.yml` file.

- `check_interval_minutes`: interval between checks for new streams in minutes (if you get rate limited, increase this number).
- `telegram_token`: Telegram bot token which will send you notifications.
- `notify_on_stream_end`: whether to send notification when stream ends.
- `twitch_usernames`: list of streamers to check for.
- `telegram_chat_ids`: list of user IDs to send notifications for (write to [@userinfobot](https://t.me/userinfobot) to get your ID).
- `apykuma`: settings for [apykuma](https://pypi.com/project/apykuma/), if you don't know what is it - don't touch it.
- `sentry`: settings for [Sentry](https://sentry.io), if you don't know what is it - don't touch it.
- `logging`: settings for logging, keep as it is, only useful for debugging.

Note that to apply changes, you need to restart the app.

## Installing for local developing

```bash
git clone https://github.com/PerchunPak/twitch-stream-notifier.git
cd twitch-stream-notifier
```

### Installing `poetry`

Next we need install `poetry` with [recommended way](https://python-poetry.org/docs/master/#installation).

If you use Linux, use command:

```bash
curl -sSL https://install.python-poetry.org | python -
```

If you use Windows, open PowerShell with admin privileges and use:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### Installing dependencies

```bash
poetry install --no-dev
```

### If something is not clear

You can always write to me!

## Thanks

This project was generated with [python-template](https://github.com/PerchunPak/python-template).

Code to check for Twitch stream was copied from https://stackoverflow.com/a/71289342.
