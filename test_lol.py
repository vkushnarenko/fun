import pytest
import asyncio
import time
import requests


from requests import Session
from async_aiohttp_tests import test_me_asynch

class SomeTrash():

    def __init__(self):
        self.api = Session()

    def get_ololo(self, **kwargs):
        response = self.api.get(url=f"http://httpbin.org/uuid", **kwargs)
        return response



## BOLD Solution with old architecture, from 10 seconds to 30 requests it goes to 5 seconds for 30 workers, 3 seconds for 10 or 5 workers

@pytest.fixture(scope="session")
def count_time():
    start_time = time.time()
    yield None
    print("--- %s seconds ---" % (time.time() - start_time))

@pytest.mark.parametrize("param", [(i,) for i in range(9999)])
def test_me(count_time, param):
    call = SomeTrash()
    response = call.get_ololo()
    #print(response.json())
    assert response.json()





# pytest -v -s test_lol.py -n auto
# 100 runs = 32 second in 1 thread vs 2 seconds aiohttp, with 10 workers it will be like 6 seonds in 10 threads
# If we combine this solution we can run 10000 requests in 20seconds, by threading 100 tests with 100 requests aiohttp
#  or we can just leave as is and get the same amount for aiohttp, by sending in asynch mode 10000 requests
# pure xdist and requests will give us - for 10k requests 6 minutes.


