# -*- coding: utf-8 -*-

__author__ = 'Helge Helo Klemetsdal'
__email__ = 'hegkleme@nmbu.no'
SUITS = ('C', 'S', 'H', 'D')
VALUES = range(1, 14)


def deck_loop():
    deck = []
    for suit in SUITS:
        for val in VALUES:
            deck.append((suit, val))
    return deck


def deck_comp():
    deck = [(suit, val) for suit in SUITS for val in VALUES]
    return deck


if __name__ == '__main__':
    if deck_loop() != deck_comp():
        print('ERROR!')
