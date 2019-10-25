# -*- coding: utf-8 -*-

__author__ = 'Helge Helo Klemetsdal'
__email__ = 'hegkleme@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.seed = seed

    def rand(self):
        a = 16807
        m = 2**31-1
        random_number = a*16807*self.seed*m
        return random_number


class ListRand:
    def __init__(self, list_of_numbers):
        self.list = list_of_numbers

    def rand(self):
        number_list = self.list
        if len(number_list) == 0:
            raise RuntimeError("Last number has been returned")
        number = number_list.pop(0)
        return number


if __name__ == "__main__":
    lcg = LCGRand(1)
    lr = ListRand([1, 2, 3])
    for _ in range(3):
        print(lcg.rand())

    for _ in range(3):
        print(lr.rand())
