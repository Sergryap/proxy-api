from pydantic import BaseModel
from typing import Any, Union
import httpx


class Balance(BaseModel):
    success: bool
    data: dict[str, Union[int, str]] = None
    error: dict[str, list[Union[int, str]]] = None


class IP(BaseModel):
    success: bool
    data: list[dict[str, Union[int, str, list[dict[str, Union[int, str]]]]]] = None
    error: dict[str, list[Union[int, str]]] = None


class OrderPrice(BaseModel):
    success: bool
    data: dict[str, Union[int, str]] = None
    error: dict[str, Union[int, str, dict[str, list[Any]]]] = None


class Services(BaseModel):
    success: bool
    data: list[dict[str, Union[int, str, list[Any]]]]


class BuyProxy(BaseModel):
    success: bool
    data: dict[str, Union[int, str]] = None
    error: dict[str, Union[int, str, dict, list]] = None


class ExistingOrder(BaseModel):
    success: bool
    data: dict[str, Union[int, str]] = None
    error: dict[str, Union[int, str, dict, list]] = None


class ProxysHTTPStatusError(httpx._exceptions.HTTPStatusError):
    pass


class ProxysRuntimeError(RuntimeError):
    pass

