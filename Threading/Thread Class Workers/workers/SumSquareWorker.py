import threading


class SumSquareWorker(threading.Thread):
    def __init__(self, n, **kwargs):
        self._n = n
        super(SumSquareWorker, self).__init__(**kwargs)
        self.start()

    def _sumSquare(self):
        s = 0
        for i in range(self._n):
            s += i**2
        print(s)

    def run(self):
        self._sumSquare()
