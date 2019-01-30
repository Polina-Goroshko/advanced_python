"""
Environment:
    system: Ubuntu 16.04.4, x86_64
    Python: 3.5.2

Task: output numbers from 0..100 in order.
First thread outputs even numbers.
Second thread outputs odd numbers.

Type of synchronization object: Semaphore.
"""
from time import sleep
from threading import Thread, Semaphore

semaphore = Semaphore(value=1)

result = []

SLEEP_TIME = 0.3  # seconds
TOTAL_RANGE = 101


def even_print():
    """
        Prints even values.
    """
    for value in range(TOTAL_RANGE):

        if value % 2 == 0:
            semaphore.acquire()

            print("'{function_name}': {value}".
                  format(function_name=even_print.__name__, value=value))
            result.append(value)

            semaphore.release()
        sleep(SLEEP_TIME)


def odd_print():
    """
        Prints odd values.
    """
    for value in range(TOTAL_RANGE):
        if value % 2 != 0:
            semaphore.acquire()

            print("'{function_name}' : {value}".
                  format(function_name=odd_print.__name__, value=value))
            result.append(value)

            semaphore.release()
        sleep(SLEEP_TIME)


def checker():
    """
        Compares a final list with an ideal one.
        In case, when they are not equal, raises an Exception.
    """
    if result != [value for value in range(TOTAL_RANGE)]:
        raise Exception


thread1 = Thread(target=even_print)
thread2 = Thread(target=odd_print)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

checker()
