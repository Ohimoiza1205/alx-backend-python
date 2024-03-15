#!/usr/bin/env python3

"""main code for multiplier"""

make_multiplier = __import__('8-make_multiplier').make_multiplier
print(make_multiplier.__annotations__)

"""main code for fun"""
fun = make_multiplier(2.22)
print("{}".format(fun(2.22)))
