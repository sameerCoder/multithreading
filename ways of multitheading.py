'''
# creating thread.
from threading import *
def display():
    for i in range(10):
        print("child")
        
t=Thread(target=display)
t.start()
t.join()

for i in range(10):
    print("main")'''
'''
# creating thead by extending thread class.
from threading import *
class MYthread(Thread):
    def run(self):
        for i in range(10):
            print("child")

t=MYthread()
t.start()
#t.join()
for i in range(10):
    print("main")
'''
# without extending thread class
from threading import *
class Test():
    def f1(self):
        for i in range(10):
            print("child")

obj=Test()
t=Thread(target=obj.f1)
#t.start()
for i in range(10):
    print("main")






















            
























