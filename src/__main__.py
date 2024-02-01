import asyncio

from loguru import logger

from src import utils
from src.config import Config
from src.db import Database
from src.logic.check_status import check_status
from src.logic.send_notification import send_notifications


async def loop() -> None:
    config = Config()

    while True:
        status = await check_status()
        await send_notifications(status)

        await asyncio.sleep(config.check_interval_minutes * 60)


async def main() -> None:
    utils.setup_logging()
    logger.info("Hello World!")

    Config()
    Database()
    utils.start_sentry()
    await utils.start_apykuma()

    await loop()


if __name__ == "__main__":
    asyncio.run(main())
