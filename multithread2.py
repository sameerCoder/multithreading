
'''
# first way of using threading.
from threading import *
def display():
    for i in range(10):
        print("child thread.")
t=Thread(target=display)

t.start()
#t.join()

for i in range(10):
    print("Main Thread.")'''
###################################################
'''
# 2 way #

from threading import *
class MyThread(Thread):
    def run(self):
        for i in range(10):
            print('child Thread')
t=MyThread()
t.start()
t.join()
for i in range(10):
    print('Main Thread')
'''
# 3 way #
from threading import *
class Test:
    def f1(self):
        for i in range(10):
            print("child Thread")
obj=Test()
t=Thread(target=obj.f1)
t.start()
for i in range(10):
    print("Main Thread.")




















            






















