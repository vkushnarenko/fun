import requests
import time

start_time = time.time()
for i in range(50):
    print(requests.get("http://httpbin.org/uuid").text)

print("--- %s seconds ---" % (time.time() - start_time))