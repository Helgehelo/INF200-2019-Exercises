# -*- coding: utf-8 -*-

__author__ = 'Helge Helo Klemetsdal'
__email__ = 'hegkleme@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.seed = seed

    def rand(self):
        a = 16807
        m = 2**31-1
        self.seed = a*self.seed % m
        return self.seed


class ListRand:
    def __init__(self, list_of_numbers):
        self.list = list_of_numbers
        self.idx = 0

    def rand(self):
        number_list = self.list
        if self.idx == len(number_list):
            raise RuntimeError("Last number has been returned")
        number = number_list[self.idx]
        self.idx += 1
        return number


if __name__ == "__main__":
    lcg = LCGRand(1)
    lr = ListRand([1, 2, 3])
    for _ in range(3):
        print(lcg.rand())

    for _ in range(3):
        print(lr.rand())

    try:
        lr.rand()
    except RuntimeError:
        print("Last number has been returned")
