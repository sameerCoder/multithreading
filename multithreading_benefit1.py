'''
# without thread
import time
def doubles(numbers):
    for n in numbers:
        time.sleep(2)
        print("Double values:",2*n)

def squares(numbers):
    for n in numbers:
        time.sleep(2)
        print("Square values:",n*n)
begintime=time.time()
numbers=[1,2,3,4,5,6]
doubles(numbers)
squares(numbers)
endtime=time.time()
print("The total time took:",endtime-begintime)
'''
########################
# 2 way with threading #
import time
from threading import *
def doubles(numbers):
    for n in numbers:
        time.sleep(2)
        print("Double value:",2*n)

def squares(numbers):
    for n in numbers:
        time.sleep(2)
        print("square value:",n*n)
begintime=time.time()
numbers=[1,2,3,4,5,6]
t1=Thread(target=doubles,args=(numbers,))
t2=Thread(target=squares,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
endtime=time.time()
print("Time took:",endtime-begintime)












































