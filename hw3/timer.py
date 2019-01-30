"""
Environment:
    system: Ubuntu 16.04.4, x86_64
    Python: 3.5.2

Task: output numbers from 0..100 in order.
First thread outputs even numbers.
Second thread outputs odd numbers.

Type of synchronization object: Timer.
"""
from threading import Timer
from time import sleep

result = []

SLEEP_TIME = 1  # seconds
TOTAL_RANGE = 101


def even_print():
    """Prints even values."""

    for value in range(TOTAL_RANGE):

        if value % 2 == 0:

            print("'{function_name}': {value}".
                  format(function_name=even_print.__name__, value=value))
            result.append(value)

            sleep(SLEEP_TIME * 2)


def odd_print():
    """Prints odd values."""

    for value in range(TOTAL_RANGE):

        if value % 2 != 0:

            print("'{function_name}' : {value}".
                  format(function_name=odd_print.__name__, value=value))
            result.append(value)

            sleep(SLEEP_TIME * 2)


def checker():
    """Compares a final list with an ideal one.
    In case, when they are not equal, raises an Exception.
    """
    if result != [value for value in range(TOTAL_RANGE)]:
        raise Exception


thread1 = Timer(0, even_print)
thread2 = Timer(SLEEP_TIME, odd_print)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

checker()
