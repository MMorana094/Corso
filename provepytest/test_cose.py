import pytest
import cose
from pytest_mock import MockerFixture, mocker

def test_sum() -> bool:
    res = cose.sum(4, 6) == 10
    res2 = cose.sum(4, 6) == 11

    assert res is True
    assert res2 is False

def test_suc() -> bool:
    #Arrange/Act
    res = cose.succ(5) == 6
    res2 = cose.succ(5) == 7
    #Assert
    assert res is True
    assert res2 is False
