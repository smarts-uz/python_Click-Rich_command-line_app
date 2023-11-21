import os
import sys


c = input('Type path:')
x = input('Name of folder:')
amount = input('Amount of folder:')
for i in range(int(amount)):
    os.makedirs(c+'\\'+x+str(i))
os.makedirs('D:\\test_examplle')
