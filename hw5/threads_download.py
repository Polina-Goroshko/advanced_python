"""Homework5: download a bunch of files using common threads"""

import os
import requests
import threading
import time

urls = ['https://www.python.org/ftp/python/3.8.0/Python-3.8.0a2.tgz',
        'https://www.python.org/ftp/python/2.7.16/Python-2.7.16rc1.tgz',
        'https://www.python.org/ftp/python/3.8.0/Python-3.8.0a1.tgz',
        'https://www.python.org/ftp/python/3.7.2/Python-3.7.2rc1.tgz',
        'https://www.python.org/ftp/python/3.6.8/Python-3.6.8rc1.tgz',
        'https://www.python.org/ftp/python/3.7.1/Python-3.7.1rc2.tgz',
        'https://www.python.org/ftp/python/3.6.7/Python-3.6.7rc2.tgz']

threads = []


def download(url):
    """Get a response from the url. Write its content to the file.

    :param url: link to download
    """
    target_file = "_".join([thread.name, os.path.basename(url)])

    response = requests.get(url=url)

    with open(target_file, "wb") as file:
        file.write(response.content)


if __name__ == "__main__":

    start_time = time.time()

    for url in urls:
        threads.append(threading.Thread(target=download, args=(url, )))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    finish_time = time.time()

    print("Common threads. Result time: {}".
          format(finish_time - start_time))
