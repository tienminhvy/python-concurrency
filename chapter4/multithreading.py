import os
import threading

import time
from threading import Thread


def cpu_waster(i: int):
    name = threading.current_thread().name
    print(f"Thread {name} is doing {i} work.")
    time.sleep(3)

def display_threads():
    print("-" * 10)
    print(f"Current process ID: {os.getpid()}")
    print(f"Thread count: {threading.active_count()}")
    print("Active threads:")
    for thread in threading.enumerate():
        print(thread)

def main(n: int):
    display_threads()

    print(f"Starting {n} CPU wasters...")
    for i in range(n):
        thread = Thread(target=cpu_waster, args=(i,))
        thread.start()

    display_threads()

if __name__ == '__main__':
    num_of_threads = 15
    main(num_of_threads)
