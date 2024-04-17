from utils import _lock
import time


class EasyBar:

    def __init__(self, task_ls: list):
        self._task_ls = task_ls
        self._f_string = ''
        self._length = 3

        self._task_count = len(self._task_ls)
        self.intervals = [100 / self._task_count * i for i in range(1, self._task_count + 1)]

    def __iter__(self):
        for i, task in enumerate(self._task_ls):
            self.update_f_string(i)
            print(self._f_string, end='')
            yield task
            time.sleep(0.2)

    def update_f_string(self, i: int):
        self._f_string = f'\r{("-" * self._length * (i + 1)): <{self._length * self._task_count}}{self.intervals[i]:.2f}% {i + 1}/{self._task_count}'


def main():
    bar = EasyBar(['task1', 'task2', 'task3', 'task4', 'task5'])

    for task in bar:
        pass

if __name__ == '__main__':
    main()
