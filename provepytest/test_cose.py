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

def test_a(mocker: MockerFixture) -> None:
    #Arrange
    mock_random_return = 6
    mocker.patch.object(cose, "random", return_value=mock_random_return)
    spy = mocker.spy(cose, "random")
    #Act
    res = cose.a()
    #Assert
    assert res is True
    assert spy.call_count == 1
    assert spy.spy_return == mock_random_return

def test_a1(mocker: MockerFixture) -> None:
    #Arrange
    mock_random_return = 4
    mocker.patch.object(cose, "random", return_value=mock_random_return)
    spy = mocker.spy(cose, "random")
    #Act
    res = cose.a()
    #Assert
    assert res is False
    assert spy.call_count == 1
    assert spy.spy_return == mock_random_return
