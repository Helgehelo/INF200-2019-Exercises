<<<<<<< Updated upstream
# -*- coding: utf-8 -*-

__author__ = 'Helge Helo Klemetsdal'
__email__ = 'hegkleme@nmbu.no'

class Board:
    def __init__(self, list1, list2, number):
        self.a = a
=======
<<<<<<< HEAD
>>>>>>> Stashed changes


=======
# -*- coding: utf-8 -*-

__author__ = 'Helge Helo Klemetsdal, Adam Julius Olof Kviman'
__email__ = 'hegkleme@nmbu.no, juliukvi@nmbu.no'


class Board:
    def __init__(self, ladders=((1, 4), (5, 16)), chutes=((9, 2), (12, 3)),
                 goal=90):

        self.ladders = ladders
        self.chutes = chutes
        self.goal = goal

    def goal_reached(self, pos):
        return True

    def position_adjustment(self, pos):
        return 1


class Player:
    def __init__(self, board):
        self.board = board

    def move(self):
        pass


class ResilientPlayer(Player):
    def __init__(self, board, extra_steps=4):
        super().__init__(board)
        self.extra_steps = extra_steps
        self.pos = 0

    def move(self):
        pass


class LazyPlayer(Player):
    def __init__(self, board, dropped_steps=4):
        super().__init__(board)
        self.dropped_steps = dropped_steps
        self.pos = 0

    def move(self):
        pass


class Simulation:
    def __init__(self, player_field=(Player, Player),
                 board=Board, seed=123, randomize_players=True):
        self.player_field = list(player_field)
        self.board = board
        self.seed = seed
        self.randomize_players = randomize_players
        self.results = []

    def single_game(self):
        return 2, "Player"

    def run_simulation(self, number_of_games):
        for i in range(number_of_games):
            self.results.append((self.single_game()))

    def get_results(self):
        return self.results

    def players_per_type(self):
        return {"Player": 10, "LazyPlayer": 22, "ResilientPlayer": 8}

    def winners_per_type(self):
        return {"Player": 10, "LazyPlayer": 22, "ResilientPlayer": 8}

    def durations_per_type(self):
        return {"Player": [1, 2, 3], "LazyPlayer": [1, 2, 3],
                "ResilientPlayer": [1, 2, 3]}
>>>>>>> pa02
