import random
import os
import string
import time

def fun1(rand):
    while True:
        key1=''.join(random.choices(string.ascii_letters+string.digits,k=rand))
        key1+=''.join(random.choices(string.ascii_letters+string.digits,k=rand))
        print(f"Key from random value is:", {key1})
        time.sleep(30)



fun1(5)





