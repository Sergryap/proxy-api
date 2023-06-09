from pydantic import BaseModel
from typing import Dict, List, Any, Union
import httpx


class Balance(BaseModel):
    success: bool
    data: Dict[str, Union[int, str]] = None
    error: Dict[str, List[Union[int, str]]] = None


class IP(BaseModel):
    success: bool
    data: List[Dict[str, Union[int, str, List[Dict[str, Union[int, str]]]]]] = None
    error: Dict[str, List[Union[int, str]]] = None


class OrderPrice(BaseModel):
    success: bool
    data: Dict[str, Union[int, str]] = None
    error: Dict[str, Union[int, str, Dict[str, List[Any]]]] = None


class Services(BaseModel):
    success: bool
    data: List[Dict[str, Union[int, str, List[Any]]]]


class BuyProxy(BaseModel):
    success: bool
    data: Dict[str, Union[int, str]] = None
    error: Dict[str, Union[int, str, Dict, List]] = None


class ExistingOrder(BaseModel):
    success: bool
    data: Dict[str, Union[int, str]] = None
    error: Dict[str, Union[int, str, Dict, List]] = None


class ProxysHTTPStatusError(httpx._exceptions.HTTPStatusError):
    pass


class ProxysRuntimeError(RuntimeError):
    pass

