from itertools import product
import pytest
from typing import Union
import calculator
from pytest_mock import MockerFixture, mocker


def test_isFree():
    res = calculator.isFree == False


def test_sum()->Union[int, float]:
    res = sum(1, 1) == 3
    res2 = sum(1, 1) == 2

def test_Mult()->Union[int, float]:
    res = calculator.Mult(5, 2) == 10
    res2 = calculator.Mult(5, 2) == 15