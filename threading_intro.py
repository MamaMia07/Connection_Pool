import threading

# threading allows us to speed up programs by executing
#multiple tasks at the SAME time. Each task woll run on its own thread
#Each thread can run simultaneously and share data with each other

#Every thread when you start it must do SOMETHING, which we can define with function
# Our threads will then target these functions.
# When we start the threads, the target functions will be run

def function1():
    for _ in range(5):
        print('ONE')

def function2():
    for _ in range(5):
        print('TWO')

def function3():
    for _ in range(5):
        print('THREE')


# if we call these functions, we see the first function call MUST complete before the next
# They are executed linearly

#function1()
#function2()
#function3()

# We execute these functions concurrently using threads! We must have a target for a thread
t1 = threading.Thread(target = function1)
t2 = threading.Thread(target = function2)
t3 = threading.Thread(target = function3)

#we have to start all threads
t1.start()
t2.start()
t3.start()

#threads can only be used ONCE!
#If you want to reuse, you must redefine thread
t1 = threading.Thread(target = function1)
t1.start()
print('Threading rules! ') #NAPIS

#if you want to 'pause' the main program until threads are done, you can!
t1 = threading.Thread(target = function1)
t1.start()
t1.join() #This pauses the main program until the thread is complete
print('Threading rules! - after .join() ')

