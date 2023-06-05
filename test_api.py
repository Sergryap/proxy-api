import asyncio
import aiohttp
import json

from environs import Env
from pprint import pprint
from with_httpx import (
    get_ip,
    get_balance,
    get_services,
    get_order_price,
    extend_existing_order,
    buy_proxy,
)


async def test_api(method, data=None):
    response = await method(**(data if data else {}))
    pprint(response)


if __name__ == '__main__':

    env = Env()
    env.read_env()
    KEY = env.str('KEY')

    loop = asyncio.new_event_loop()
    # loop.run_until_complete(
    #     test_api(
    #         buy_proxy,
    #         data={
    #             'key': KEY,
    #             'service': 3,
    #             'count': 1,
    #             'country': 'DE',
    #             'period': 30
    #         }
    #     )
    # )
    loop.run_until_complete(test_api(get_services))
    # loop.run_until_complete(test_api(get_ip, {'key': KEY}))
