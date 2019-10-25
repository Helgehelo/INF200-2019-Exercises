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
