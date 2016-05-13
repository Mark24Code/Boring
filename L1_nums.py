import cProfile
import time


class Timer(object):
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.total = None

    def start(self):
        self.start_time = time.time()

    def end(self):
        self.end_time = time.time()

    def total(self):
        self.total = self.end_time - self.start_time
        return self.total

    def result(self,name=None):
        self.total = self.end_time - self.start_time
        if not name:
            name = ''
        print('===== Time {} ====='.format(name))
        print('start:', self.start_time)
        print('end:', self.end_time)
        print('total:', self.total)
        print('================')


def main():
    count = 10 ** 5
    nums = []


    timer = Timer()

    timer.start()
    for i in range(count):
        nums.append(i)
    nums.reverse()
    timer.end()
    timer.result('demo1')

    timer1 = Timer()
    timer1.start()
    for i in range(count):
        nums.insert(0,i)
    timer1.end()
    timer1.result("demo2")


cProfile.run('main()')