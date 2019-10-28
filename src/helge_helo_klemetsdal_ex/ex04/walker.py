# -*- coding: utf-8 -*-

__author__ = 'Helge Helo Klemetsdal'
__email__ = 'hegkleme@nmbu.no'

import random as rd


class Walker:
    def __init__(self, initial_position, home_position):
        self.position = initial_position
        self.home = home_position
        self.steps = 0

    def move(self):
        movement = rd.randint(-1, 1)
        while movement == 0:
            movement = rd.randint(-1, 1)
        self.position += movement
        self.steps += 1

    def is_at_home(self):
        if self.position == self.home:
            return True
        else:
            return False

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.steps


def simulating_the_walker(simulations, list_of_distances):
    for distance in list_of_distances:
        steps_list = []
        for walks in range(simulations):
            walk = Walker(0, distance)
            while walk.is_at_home() is False:
                walk.move()
            steps_list.append(walk.steps)
        print(f"Distance: {distance:3} -> Path lengths: {steps_list}")


if __name__ == "__main__":
    simulating_the_walker(5, [1, 2, 5, 10, 20, 50, 100])
