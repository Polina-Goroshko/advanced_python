"""
Environment:
    system: Ubuntu 16.04.4, x86_64
    Python: 3.5.2

Task: output numbers from 0..100 in order.
First thread outputs even numbers.
Second thread outputs odd numbers.

Type of synchronization object: Condition.
"""
from time import sleep
from threading import Thread, Condition

condition = Condition()

result = []

SLEEP_TIME = 0.01  # seconds
TOTAL_RANGE = 101


def even_print():
    """
        Prints even values. Acts as a producer.
    """
    for value in range(TOTAL_RANGE):

        if value % 2 == 0:
            sleep(SLEEP_TIME)
            condition.acquire()

            print("'{function_name}': {value}".
                  format(function_name=even_print.__name__, value=value))
            result.append(value)

            condition.notify()
            condition.release()


def odd_print():
    """
        Prints odd values. Acts as a consumer.
    """
    for value in range(TOTAL_RANGE):
        if value % 2 != 0:
            condition.acquire()
            condition.wait()

            print("'{function_name}' : {value}".
                  format(function_name=odd_print.__name__, value=value))
            result.append(value)

            condition.release()


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
