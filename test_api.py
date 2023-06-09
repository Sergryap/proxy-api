import asyncio
import httpx

from environs import Env
from pprint import pprint
import proxy_api


async def test_api(method, data=None):
    async with httpx.AsyncClient() as session:
        response = await method(session, **(data if data else {}))
        pprint(response.dict())


if __name__ == '__main__':

    env = Env()
    env.read_env()
    KEY = env.str('KEY')

    loop = asyncio.new_event_loop()
    # loop.run_until_complete(
    #     test_api(
    #         proxy_api.buy_proxy,
    #         data={
    #             'key': KEY,
    #             'service': 3,
    #             'count': 1,
    #             'country': 'DE',
    #             'period': 30
    #         }
    #     )
    # )
    loop.run_until_complete(test_api(proxy_api.get_services))
    # loop.run_until_complete(test_api(proxy_api.get_ip, {'key': KEY}))
    # loop.run_until_complete(test_api(proxy_api.get_order_price, {'service': 1, 'count': 1}))
