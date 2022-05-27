from typing import Union
from math import *
import pytest
from pytest_mock import MockerFixture

def sum(a: Union[int, float], b:Union[int, float]) ->Union[int, float] :
    c = a + b
    return c

def sub(a: Union[int, float], b:Union[int, float]) ->Union[int, float] :
    return a - b

def Mult(a: Union[int, float], b:Union[int, float]) ->Union[int, float] :
    return a * b

def Div(a: Union[int, float], b:Union[int, float]) ->Union[int, float] :
    return a / b

print("Hello, choice a function :")
print("1) Sum ")
print("2) Sub ")
print("3) Mult ")
print("4) Div ")
print("5) Sqrt ")
print(" ")
print(" ")
print("0) exit ")
isFree = True
while isFree == True :
    choice = int(input("Select function : "))
    isFree = False
    if choice == 0 :
        exit()
    if choice == 1 :
        a = int(input("Insert first number : "))
        b = int(input("Insert Second Number : "))
        Sum = sum(a, b)
        print("la somma dei numeri interessati e' : " + str(Sum))
        isFree = True
    if choice == 2 :
        a = int(input("Insert first number : "))
        b = int(input("Insert Second Number : "))
        Sub = sub(a, b)
        print("la sottrazione dei numeri interessati e' : " + str(Sub))
        isFree = True
    if choice == 3 :
        a = int(input("Insert first number : "))
        b = int(input("Insert Second Number : "))
        Mult = Mult(a, b)
        print("la moltiplicazione dei numeri interessati e' : " + str(Mult))
        isFree = True

    if choice == 4 :
        a = int(input("Insert first number : "))
        b = int(input("Insert Second Number : "))
        while b <= 0 :
            b = int(input("Insert Second Number : "))
        Div = Div(a, b)
        print("la divisione dei numeri interessati e' : " + str(Div))
        isFree = True

    if choice == 5:
        a = int(input("Insert number : "))
        while a < 1 :
            a = int(input("Insert Number : "))
        rad = sqrt(a)
        print("la radice quadrata del numero interessato e' : " + str(rad))
        isFree = True
