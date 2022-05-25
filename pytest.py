from random import random
import pytest

def a() -> bool:
    return random() >0.5

def b() -> int:
    is_a = a()
    if is_a:
        return 10
    else:
        return 20

