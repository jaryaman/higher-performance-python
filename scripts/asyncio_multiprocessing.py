import asyncio
from aiohttp import request
from aiomultiprocess import Pool
import random
from time import process_time

async def makerandom(args):
    idx, threshold = args
    print(f"Initiated makerandom({idx})")
    i = random.randint(0, 10)
    while i <= threshold:
        print(f"makerandom({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)  # mimics an IO-bound process with an uncertain wait time
        i = random.randint(0, 10)
    print(f"--> Finished: makerandom({idx}) == {i}")
    return i

async def get(url):
    async with request("GET", url) as response:
        return await response.read()


async def main_get():  # example from the docs
    urls = ["https://www.google.com"]
    async with Pool() as pool:
        async for result in pool.map(get, urls):
            print(result)

async def main_makerandom():
    r = []
    async with Pool(2) as pool:
        async for result in pool.map(makerandom, [(i, 10 - i - 1) for i in range(6)]):
            r.append(result)
    return r

if __name__ == '__main__':
    s = process_time()
    results = asyncio.run(main_makerandom())  # 1 process = 45.66s, 2 processes = 19.27s
    print(f'Time elapsed = {process_time() - s:.2f}s')
    print('Results:')
    print(results)