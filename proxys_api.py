

async def get_balance(session, *, key):

    """Проверка баланса пользователя"""

    url = f"http://proxys.io/ru/api/v2/balance"
    params = {'key': key}
    async with session.get(url, params=params) as response:
        response.raise_for_status()
        return await response.text()


async def get_ip(session, *, key):

    """Запрос ip адресов пользователя"""

    url = f"http://proxys.io/ru/api/v2/ip"
    params = {'key': key}
    async with session.get(url, params=params) as response:
        response.raise_for_status()
        return await response.text()


async def get_order_price(session, *, service, count, country='RU', period=30):

    """Запрос цены нового заказа"""

    url = f"http://proxys.io/ru/api/v2/price"
    params = {
        'service': service,
        'count': count,
        'country': country,
        'period': period
    }
    async with session.get(url, params=params) as response:
        response.raise_for_status()
        return await response.text()


async def get_services(session, *, tariff=1, description=0):

    """Запрос доступных для аренды типов ip адресов"""

    url = f"http://proxys.io/ru/api/v2/services"
    params = {
        'tariff': tariff,
        'description': description,
    }
    async with session.get(url, params=params) as response:
        response.raise_for_status()
        return await response.text()


async def buy_proxy(session, *, key, service=1, count=1, country='RU', period=30):

    """Покупка новых прокси"""

    url = f"http://proxys.io/ru/api/v2/buy"
    body = {
        'key': key,
        'service': service,
        'count': count,
        'country': country,
        'period': period
    }
    async with session.post(url, json=body) as response:
        response.raise_for_status()
        return await response.text()


async def extend_existing_order(session, *, key, order_id):

    """Продление существующего заказа"""

    url = f"http://proxys.io/ru/api/v2/extending"
    body = {
        'key': key,
        'order_id': order_id,
    }
    async with session.post(url, json=body) as response:
        response.raise_for_status()
        return await response.text()
