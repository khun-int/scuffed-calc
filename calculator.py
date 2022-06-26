#!/usr/bin/python 
import time as cum
import os
import keyboard


def calculate():
    if mode == 1:
        print("")
        print("Addition")
        print("")
        print(num1+num2)
        print("")
        input("press [enter] to continue, [k] to quit")
    elif mode == 2:
        print("")
        print("Subtraction")
        print("")
        print(num1-num2)
        print("")
        input("press [enter] to continue, [k] to quit")
    else:
        print("")
        print("error")

if __name__ == "__main__":
    while True:
            print("[Calculator]")
            mode = int(input("[1]Addition" + "    [2]Subtract >> "))
            num1 = int(float(input(">>")))
            num2 = int(float(input(">>")))
            calculate()
            if keyboard.is_pressed('k'):
                break 

