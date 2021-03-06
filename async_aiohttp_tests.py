import asyncio
import time
from aiohttp import ClientSession

async def fetch(url, session):
    async with session.get(url) as response:
        return await response.json()

async def run(r):
    url = "http://httpbin.org/uuid"
    tasks = []

    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with ClientSession() as session:
        for i in range(r):
            task = asyncio.ensure_future(fetch(url.format(i), session))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        # you now have all response bodies in this variable
        print_responses(responses)

    return responses

def print_responses(result):
    print(result)

def test_me_asynch():
    start_time = time.time()
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(100))
    loop.run_until_complete(future)

    print("--- %s seconds ---" % (time.time() - start_time))

