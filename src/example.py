'''
An example of Python file
'''

import os
import time

class FooBarObserver:
    def __init__(self, path_of_file_to_watch):
        self.path = path_of_file_to_watch
        self.observers = set()
        self._last_size = 0

    def register(self, observer):
        self.observers.add(observer)
    def unregister(self, observer):
        self.observers.discard(observer)

    def check_forever(self):
        while True:
            self.check_file()
            time.sleep(0.1)

    def check_file(self):
        size = os.stat(self.path).st_size
        if size != self._last_size:
            self._last_size = size
            self.dispatch(size)

    def dispatch(self, size):
        for observer in self.observers:
            observer.update(size)

