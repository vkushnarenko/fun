import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
from timeit import default_timer

START_TIME = default_timer()

def fetch(session):
    base_url = "http://httpbin.org/uuid"
    with session.get(base_url) as response:
        data = response.text

        elapsed = default_timer() - START_TIME
        time_completed_at = "{:5.2f}s".format(elapsed)
        print(time_completed_at)
        print(response.text)

        return data

async def get_data_asynchronous():
    print("{0:<30} {1:>20}".format("File", "Completed at"))
    with ThreadPoolExecutor(max_workers=50) as executor:
        with requests.Session() as session:
            # Set any session parameters here before calling `fetch`
            loop = asyncio.get_event_loop()
            START_TIME = default_timer()
            tasks = [
                loop.run_in_executor(
                    executor,
                    fetch,
                    (session) # Allows us to pass in multiple arguments to `fetch`
                )
                for csv in range(50)
            ]
            response = await asyncio.gather(*tasks)



loop = asyncio.get_event_loop()
future = asyncio.ensure_future(get_data_asynchronous())
loop.run_until_complete(future)
print(future.result())

# NOT WORKING AS EXPECTED