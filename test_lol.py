import pytest
import asyncio
import time
import requests


from requests import Session
from requests_futures.sessions import FuturesSession
from aiohttp import ClientSession

from async_aiohttp_tests import test_me_asynch

class SomeTrash():

    def __init__(self):
        self.api = Session()
        self.api2 = ClientSession()
        self.api3 =FuturesSession()

    def get_ololo(self, **kwargs):
        response = self.api.get(url=f"http://httpbin.org/uuid", **kwargs)
        return response

    async def get_ololo2(self, **kwargs):
        response = await self.api2.get(url=f"http://httpbin.org/uuid", **kwargs)
        return response

    def get_ololo3(self, **kwargs):
        response = self.api3.get(url=f"http://httpbin.org/uuid", **kwargs)
        return\
            response.result()


## BOLD Solution with old architecture, from 10 seconds to 30 requests it goes to 5 seconds for 30 workers, 3 seconds for 10 or 5 workers

@pytest.fixture(scope="session")
def count_time():
    start_time = time.time()
    yield None
    print("--- %s seconds ---" % (time.time() - start_time))

@pytest.mark.parametrize("param", [(i,) for i in range(99)])
def test_me(count_time, param):
    call = SomeTrash()
    response = call.get_ololo()
    #print(response.json())
    assert response.json()

def test_some():
    test_me_asynch()
#pytest -v -s test_lol.py -n 11


# 100 runs = 32 second in 1 thread vs 2 seconds aiohttp, with 10 workers it will be like 6 seonds in 10 threads


