#! -*- coding: utf-8 -*-

import io
import time
import re
import os, fnmatch
import sys

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



file1 = open("file.ini", 'r')
lines = file1.readlines()
try:
    list = []
    nameCount = []
    indiviualName = []
    data = []
    print("Enter Try")
    for line in reversed(lines):
        list = re.split(r"\t+", line)

    linea = list[0]
    linea = linea.replace("[","")
    linea = linea.replace("]","")
    names = linea.split(",")

    for name in names:
        if (not indiviualName):
            indiviualName.append(name)
            nameCount.append(1)
        elif (name in indiviualName):
            nameCount[indiviualName.index(name)] += 1
        else:
            indiviualName.append(name)
            nameCount.append(1)

    for name in indiviualName:
        data.append([name, nameCount[indiviualName.index(name)]])

    data = sorted(data, key=lambda data: data[1], reverse = True)
    print(data)
except Exception as e:
    # Closing file
    print("Fallo: ",e)
    file1.close()