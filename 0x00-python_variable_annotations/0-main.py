#!/usr/bin/env python3
add = __import__('0-add').add

"""main file for task 0"""

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)