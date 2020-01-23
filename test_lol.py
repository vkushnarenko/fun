import pytest
import asyncio
import time
import requests


from requests import Session

#FIXME This approach provide the ability to to run tests as load once with aiohttp lib.
from async_aiohttp_tests import test_me_asynch
from concurrent.futures import ThreadPoolExecutor
from timeit import default_timer

class SomeTrash():

    def __init__(self, session=Session()):
        self.api = session

    def get_ololo(self, **kwargs):
        response = self.api.get(url=f"http://httpbin.org/uuid", **kwargs)
        return response



## BOLD Solution with old architecture, from 10 seconds to 30 requests it goes to 5 seconds for 30 workers, 3 seconds for 10 or 5 workers

@pytest.fixture(scope="session")
def count_time():
    start_time = time.time()
    yield None
    print("--- %s seconds ---" % (time.time() - start_time))


#FIXME This approach provide the ability to to run tests as load once with xdist and
@pytest.mark.parametrize("param", [(i,) for i in range(10)])
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





##FIXME This approach will provide ability to run old tests, in asynch way to make some load
async def run_tests_asynch(test_list):
    # Note: max_workers is set to 10 simply for this example,
    # you'll have to tweak with this number for your own projects
    # as you see fit
    results =[]
    with ThreadPoolExecutor() as executor:
        with requests.Session() as session:
            # Set any session parameters here before calling `fetch`

            # Initialize the event loop
            loop = asyncio.get_event_loop()

            # Use list comprehension to create a list of
            # tasks to complete. The executor will run the `fetch`
            # function for each csv in the csvs_to_fetch list
            tasks = [
                loop.run_in_executor(
                    executor,
                    test,
                    session  # Allows us to pass in multiple arguments to `fetch`
                )
                for test in test_list
            ]

            # Initializes the tasks to run and awaits their results
            for result in await asyncio.gather(*tasks):
                results.append(result)

    return results

def test_simple(session):
    call = SomeTrash(session)
    response = call.get_ololo()
    print(response.json())
    assert response.json()
    return response

@pytest.mark.parametrize("test_name, load_value", [(test_simple, 20)])
def test_load_for(test_name, load_value):
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run_tests_asynch([test_name for _ in range(load_value)]))
    loop.run_until_complete(future)
    print(future.result())