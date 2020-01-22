import pytest
import asyncio
import time
import requests


from requests import Session
from aiohttp import ClientSession

class SomeTrash():

    def __init__(self):
        self.api = Session()
        self.api2 = ClientSession()

    def get_ololo(self, **kwargs):
        response = self.api.get(url=f"http://httpbin.org/uuid", **kwargs)
        return response

    async def get_ololo2(self, **kwargs):
        response = await self.api2.get(url=f"http://httpbin.org/uuid", **kwargs)
        return response


def test_me():
    call = SomeTrash()
    response = call.get_ololo()
    #print(response.json())
    assert response.json()

@pytest.mark.asyncio
async def test_me2():
    call = SomeTrash()
    response = await call.get_ololo2()
    # print(response.json())
    assert response.json()


def test_multicall():
    start_time = time.time()
    for i in range(10):
        test_me()
    print("--- %s seconds ---" % (time.time() - start_time))

@pytest.mark.asyncio
async def test_async_multicall():
    start_time = time.time()
    for i in range(10):
       res = await test_me2()
    print("--- %s seconds ---" % (time.time() - start_time))

# lol this will not work )