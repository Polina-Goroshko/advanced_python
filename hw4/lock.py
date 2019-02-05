"""
Task: output numbers from 0..100 in order.
First process outputs even numbers.
Second process outputs odd numbers.
Any synchronization object can be used.
"""

import multiprocessing
import logging
from time import sleep

SLEEP_TIME = 0.1  # seconds
TOTAL_RANGE = 101


def even_print(lock, result):
    """Prints even values."""
    for value in range(TOTAL_RANGE):
        with lock:
            if value % 2 == 0:
                print("'{function_name}': {value}".
                      format(function_name=even_print.__name__, value=value))
                result.append(value)
        sleep(SLEEP_TIME)


def odd_print(lock, result):
    """Prints odd values."""
    for value in range(TOTAL_RANGE):
        with lock:
            if value % 2 != 0:
                print("'{function_name}' : {value}".
                      format(function_name=odd_print.__name__, value=value))
                result.append(value)
        sleep(SLEEP_TIME)


def checker():
    """Compares a final list with an ideal one.

    Note: in case, when they are not equal, notifies about it.
    """
    if result[:] != [value for value in range(TOTAL_RANGE)]:
        logging.fatal("FAIL")
    else:
        logging.info("PASS")


if __name__ == '__main__':

    lock = multiprocessing.Lock()
    result = multiprocessing.Manager().list()

    logging.basicConfig(level=logging.INFO)

    thread1 = multiprocessing.Process(target=even_print, args=(lock, result))
    thread2 = multiprocessing.Process(target=odd_print, args=(lock, result))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    checker()
