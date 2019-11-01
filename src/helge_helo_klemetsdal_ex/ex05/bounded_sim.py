# -*- coding: utf-8 -*-

__author__ = 'Helge Helo Klemetsdal'
__email__ = 'hegkleme@nmbu.no'
from .walker_sim import Walker, Simulation
import random as rd


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
           The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        self.left_limit = left_limit
        self.right_limit = right_limit
        super().__init__(start, home)

    def move(self):
        movement = rd.randint(0, 1)
        if movement == 0:
            self.position -= 1
        else:
            self.position += movement

        self.steps += 1
        if self.get_position() > self.right_limit:
            self.position = self.right_limit - 1

        if self.get_position() < self.left_limit:
            self.position = self.left_limit + 1


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        self.left_limit = left_limit
        self.right_limit = right_limit
        super().__init__(start, home, seed)

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """

        walk = BoundedWalker(self.start, self.home, self.left_limit,
                             self.right_limit)
        while walk.is_at_home() is False:
            walk.move()
        return walk.get_steps()


if __name__ == "__main__":
    left_boundaries = [0, -10, -100, -1000, -10000]
    right_boundary = 20
    for left_boundary in left_boundaries:
        sim = BoundedSimulation(0, 20, 1, left_boundary, right_boundary)
        print(f"Left boundary: {left_boundary} "
              f"Walks : {[sim.single_walk() for _ in range(20)]}")
