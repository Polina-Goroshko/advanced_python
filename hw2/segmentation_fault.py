"""
Environment:
    system: Ubuntu 16.04.4, x86_64
    Python: 3.5.2
Task: (Python3) write script which causes segmentation fault
      (use only Python standard library)
Solution: 1. to shorten the maximum size of the process stack
          2. to reach it with a recursion function
"""

import resource


def recursion(variable: int):
    """Infinite recursion

    :param variable
    """
    recursion(variable + 1)


print("(soft, hard) limits {} of 'RLIMIT_STACK'".
      format(resource.getrlimit(resource.RLIMIT_STACK)))

resource.setrlimit(resource.RLIMIT_STACK, (10, resource.RLIM_INFINITY))

print("(soft, hard) limits {} of 'RLIMIT_STACK'".
      format(resource.getrlimit(resource.RLIMIT_STACK)))

recursion(0)
