import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
from timeit import default_timer

START_TIME = default_timer()

def fetch(session):
    base_url = "http://httpbin.org/uuid"
    with session.get(base_url) as response:
        data = response.text
        if response.status_code != 200:
            print("FAILURE::{0}")
        elapsed = default_timer() - START_TIME
        time_completed_at = "{:5.2f}s".format(elapsed)
        print(f"{_} === {time_completed_at}")
        return data


async def get_data_asynchronous(number):
    # Note: max_workers is set to 10 simply for this example,
    # you'll have to tweak with this number for your own projects
    # as you see fit
    with ThreadPoolExecutor() as executor:
        with requests.Session() as session:
            # Set any session parameters here before calling `fetch`

            # Initialize the event loop
            loop = asyncio.get_event_loop()

            # Set the START_TIME for the `fetch` function
            START_TIME = default_timer()

            # Use list comprehension to create a list of
            # tasks to complete. The executor will run the `fetch`
            # function for each csv in the csvs_to_fetch list
            tasks = [
                loop.run_in_executor(
                    executor,
                    fetch,
                    *(session, _)  # Allows us to pass in multiple arguments to `fetch`
                )
                for _ in range(number)
            ]

            # Initializes the tasks to run and awaits their results
            for response in await asyncio.gather(*tasks):
                pass

def main():
    # Simple for now
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(get_data_asynchronous(100))
    loop.run_until_complete(future)

main()