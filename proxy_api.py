import httpx
import api_objects


async def get_balance(session, key):
    """User balance check

    Args:
        session: httpx.AsyncClient instance
        key (str): user access key
    Returns:
        the user balance as a Balance instance
    """

    url = 'http://proxys.io/ru/api/v2/balance'
    params = {'key': key}
    response = await session.get(url, params=params, follow_redirects=True)
    await __proxy_raise_for_status(response)
    return api_objects.Balance.parse_raw(response.text)


async def get_ip(session, key):
    """Request of user's ip addresses

    Args:
        session: httpx.AsyncClient instance
        key (str): user access key
    Returns:
        the user's ip addresses as an IP instance
    """

    url = 'http://proxys.io/ru/api/v2/ip'
    params = {'key': key}
    response = await session.get(url, params=params, follow_redirects=True)
    await __proxy_raise_for_status(response)
    return api_objects.IP.parse_raw(response.text)


async def get_order_price(session, service, count, country='RU', period=30):
    """Query for check order price

    Args:
        session: httpx.AsyncClient instance
        service (int): ip type
        count (int): ip count
        country (str): ip country
        period (int): rental period
    Returns:
        The user order price as an OrderPrice instance
    """

    url = 'http://proxys.io/ru/api/v2/price'
    params = {
        'service': service,
        'count': count,
        'country': country,
        'period': period
    }
    response = await session.get(url, params=params, follow_redirects=True)
    await __proxy_raise_for_status(response)
    return api_objects.OrderPrice.parse_raw(response.text)


async def get_services(session, tariff=1, description=0):
    """Request for available types of ip addresses, tariffs, countries

    Args:
        session: httpx.AsyncClient instance
        tariff (int): show tariff
        description (int): show description
    Returns:
        The available types of ip addresses, tariffs, countries as a Services instance
    """

    url = 'http://proxys.io/ru/api/v2/services'
    params = {
        'tariff': tariff,
        'description': description,
    }
    response = await session.get(url, params=params, follow_redirects=True)
    await __proxy_raise_for_status(response)
    return api_objects.Services.parse_raw(response.text)


async def buy_proxy(session, key, service=1, count=1, country='RU', period=30):
    """Query for purchase proxy

    Args:
        session: httpx.AsyncClient instance
        key (str): user access key
        service (int): ip type
        count (int): quantity of purchase proxy
        country (str): ip country
        period (int): rental period
    Returns:
        The purchased proxies as a BuyProxy instance
    """

    url = 'http://proxys.io/ru/api/v2/buy'
    body = {
        'key': key,
        'service': service,
        'count': count,
        'country': country,
        'period': period
    }
    response = await session.post(url, json=body, follow_redirects=True)
    await __proxy_raise_for_status(response)
    return api_objects.BuyProxy.parse_raw(response.text)


async def extend_existing_order(session, key, order_id):
    """Query for extension of the order for 30 days

    Args:
        session: httpx.AsyncClient instance
        key (str): user access key
        order_id (int): extended order id
    Returns:
        The extended order as a ExistingOrder instance
    """

    url = 'http://proxys.io/ru/api/v2/extending'
    body = {
        'key': key,
        'order_id': order_id,
    }
    response = await session.post(url, json=body, follow_redirects=True)
    await __proxy_raise_for_status(response)
    return api_objects.ExistingOrder.parse_raw(response.text)


async def __proxy_raise_for_status(response: httpx._models.Response):

    request = response._request
    if request is None:
        raise api_objects.ProxysRuntimeError(
            "Cannot call `raise_for_status` as the request "
            "instance has not been set on this response."
        )

    if response.is_success:
        return

    if response.has_redirect_location:
        message = (
            "{error_type} '{0.status_code} {0.reason_phrase}' for url '{0.url}'\n"
            "Redirect location: '{0.headers[location]}'\n"
            "For more information check: https://httpstatuses.com/{0.status_code}"
        )
    else:
        message = (
            "{error_type} '{0.status_code} {0.reason_phrase}' for url '{0.url}'\n"
            "For more information check: https://httpstatuses.com/{0.status_code}"
        )

    status_class = response.status_code // 100
    error_types = {
        1: "Informational response",
        3: "Redirect response",
        4: "Client error",
        5: "Server error",
    }
    error_type = error_types.get(status_class, "Invalid status code")
    message = message.format(response, error_type=error_type)
    raise api_objects.ProxysHTTPStatusError(message, request=request, response=response)
