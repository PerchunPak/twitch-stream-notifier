import typing as t

import aiohttp
from loguru import logger

from src.config import Config


async def check_status() -> t.Dict[str, bool]:
    """Copied from https://stackoverflow.com/a/71289342.

    Returns:
        A dict, where keys are twitch usernames (from config) and values are
        booleans which indicate whether the user is streaming or not.
    """
    config = Config()
    result: t.Dict[str, bool] = {}

    async with aiohttp.ClientSession() as session:
        for username in config.twitch_usernames:
            logger.debug(f"Checking {username=}...")
            query = 'query {\n  user(login: "' + username + '") {\n    stream {\n      id\n    }\n  }\n}'

            async with session.post(
                "https://gql.twitch.tv/gql",
                data={"query": query, "variables": {}},
                headers={"client-id": "kimne78kx3ncx6brgo4mv6wki5h1ko"},
            ) as response:
                answer = await response.json()
                logger.debug(f"{answer=}")
                result[username] = True if answer["data"]["user"]["stream"] else False

    return result
