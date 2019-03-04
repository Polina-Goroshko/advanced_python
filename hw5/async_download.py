"""Homework5: download a bunch of files using 'asyncio', 'aiohttp'"""

import aiohttp
import asyncio
import os
import time

urls = ['https://www.python.org/ftp/python/3.8.0/Python-3.8.0a2.tgz',
        'https://www.python.org/ftp/python/2.7.16/Python-2.7.16rc1.tgz',
        'https://www.python.org/ftp/python/3.8.0/Python-3.8.0a1.tgz',
        'https://www.python.org/ftp/python/3.7.2/Python-3.7.2rc1.tgz',
        'https://www.python.org/ftp/python/3.6.8/Python-3.6.8rc1.tgz',
        'https://www.python.org/ftp/python/3.7.1/Python-3.7.1rc2.tgz',
        'https://www.python.org/ftp/python/3.6.7/Python-3.6.7rc2.tgz']

tasks = []


async def download(session, url):
    """Get a response from the url. Write its content to the file.

    :param session:
    :param url: link to download
    """
    async with session.get(url) as response:
        content = await response.read()

        with open("Asyncio_{}".format(os.path.basename(url)), 'wb') as file:
            file.write(content)


async def start():
    """Create a session and run awaitable objects concurrently"""
    async with aiohttp.ClientSession() as session:

        for url in urls:
            tasks.append(download(session, url))

        await asyncio.gather(*tasks)


if __name__ == "__main__":

    start_time = time.time()
    asyncio.run(start())
    finish_time = time.time()

    print("Asyncio, aiohttp. Result time: {}".
          format(finish_time - start_time))
