"""
Task: output numbers from 0..100 in order.
First process outputs even numbers.
Second process outputs odd numbers.
Any synchronization object can be used.
"""

import logging
import multiprocessing
from time import sleep

SLEEP_TIME = 0.1  # seconds
TOTAL_RANGE = 101


def even_print(lock):
    """Prints even values."""
    for value in range(TOTAL_RANGE):
        with lock:
            if value % 2 == 0:
                print("'{function_name}': {value}".
                      format(function_name=even_print.__name__, value=value))
        sleep(SLEEP_TIME)


def odd_print(lock):
    """Prints odd values."""
    for value in range(TOTAL_RANGE):
        with lock:
            if value % 2 != 0:
                print("'{function_name}' : {value}".
                      format(function_name=odd_print.__name__, value=value))
        sleep(SLEEP_TIME)


def start():

    lock = multiprocessing.Lock()

    logging.basicConfig(level=logging.INFO)

    process1 = multiprocessing.Process(target=even_print, args=(lock,))
    process2 = multiprocessing.Process(target=odd_print, args=(lock,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
