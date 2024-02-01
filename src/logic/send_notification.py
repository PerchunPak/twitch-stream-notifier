import aiohttp
from loguru import logger

from src.config import Config
import typing as t


async def send_notifications(status: t.Dict[str, bool]) -> None:
    config = Config()

    message = ""
    for username, is_streaming in status.items():
        if is_streaming:
            message += f"🟢 {username} is streaming!\n"
        else:
            if config.notify_on_stream_end:
                message += f"🔴 {username} stopped streaming.\n"

    if not message:
        return

    async with aiohttp.ClientSession() as session:
        for chat_id in config.telegram_chat_ids:
            response = await session.post(
                f"https://api.telegram.org/bot{config.telegram_token}/sendMessage",
                json={"chat_id": chat_id, "text": message},
            )

            assert response.status == 200, await response.text()
