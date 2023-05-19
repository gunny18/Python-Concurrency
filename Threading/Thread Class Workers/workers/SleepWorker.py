import threading
import time


class SleepWorker(threading.Thread):
    def __init__(self, n, **kwargs):
        self._n = n
        super(SleepWorker, self).__init__(**kwargs)
        self.start()

    def _sleep(self):
        time.sleep(self._n)

    def run(self):
        self._sleep()
