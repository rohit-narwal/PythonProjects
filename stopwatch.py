import time
from pynput.keyboard import *

print("Press Enter to start!!!")
def stopwatch():
    start = 0
    while True:
        time.sleep(1)
        print(start)
        start += 1
if (Key.esc):
    stopwatch()
else:
    print("Enter correct key!!!")


