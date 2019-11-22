# -*- coding: utf-8 -*-

__author__ = 'Helge Helo Klemetsdal, Adam Julius Olof Kviman'
__email__ = 'hegkleme@nmbu.no, juliukvi@nmbu.no'

import random


class Board:

    def __init__(self, ladders=((1, 40), (8, 10), (36, 52), (43, 62), (49, 79),
                                (65, 82), (68, 85)),
                 chutes=((24, 5), (33, 3), (42, 30), (56, 37), (64, 27),
                         (74, 12), (87, 70)),
                 goal=90):
        """Class that handles the game board.

        Parameters
        ----------
        ladders : list or tuple
             the ladders on the board
        chutes : list or tuple
             the chutes on the board
        goal : int
            the position of the goal on the board
        """
        self.ladders = ladders
        self.chutes = chutes
        self.goal = goal

    def goal_reached(self, pos) -> bool:
        """Checks if a player has reached the goal

        Parameters
        ----------
        pos : int
            the position of the player

        Return
        ------
        Bool
            True if goal reached otherwise False
        """
        if pos >= self.goal:
            return True
        else:
            return False

    def position_adjustment(self, pos):
        """Checks if a player is on a ladder or chute. If it is, the difference
        between its current position to the position it needs to move is
        returned

        Parameter
        ---------
        pos : int
            the position of the player

        Returns
        -------
        int
            the difference between the current position to the new position"""
        for j in self.ladders:
            if j[0] == pos:
                difference = j[1]-j[0]
                return difference
        for j in self.chutes:
            if j[0] == pos:
                difference = j[1]-j[0]
                return difference
        return 0


class Player:

    def __init__(self, board=Board()):
        self.board = board
        self.pos = 0
    """Class that handles the Players on the board
    Parameters
    ----------
    board - Board() object
        choose what kind of board this player shall play on
    """

    def move(self):
        """Moves the Player"""
        self.pos += random.randint(1, 6)
        self.pos += self.board.position_adjustment(self.pos)


class ResilientPlayer(Player):
    def __init__(self, board, extra_steps=1):
        super().__init__(board)
        self.extra_steps = extra_steps
        self.chutes_checker = False

    """Subclass of Player that takes extra steps on the next move after
    going down a chute

    Parameters
    ----------
    board - Board() object
        choose what kind of board this player shall play on
    extra_steps - int
        number of steps to add
    """

    def move(self):
        """ResilientPlayer first checks if it climbed a ladder last move, it
         then executes the new move depending on the answer"""
        if self.chutes_checker:
            random_number = random.randint(1, 6)
            self.pos += (random_number + self.extra_steps)
            if self.board.position_adjustment(self.pos) < 0:
                self.chutes_checker = True
            else:
                self.chutes_checker = False
            self.pos += self.board.position_adjustment(self.pos)
        else:
            self.pos += random.randint(1, 6)
            if self.board.position_adjustment(self.pos) < 0:
                self.chutes_checker = True
            else:
                self.chutes_checker = False
            self.pos += self.board.position_adjustment(self.pos)


class LazyPlayer(Player):
    def __init__(self, board, dropped_steps=1):
        super().__init__(board)
        self.dropped_steps = dropped_steps
        self.ladder_checker = False

    """Subclass of Player that takes less steps on the next move after
    climbing a ladder

    Parameters
    ----------
    board - Board() object
        choose what kind of board this player shall play on
    dropped_steps - int
        number of steps to drop
    """

    def move(self):
        """LazyPLayer first checks if it climbed a ladder last move, it then
         executes the new move depending on the answer"""
        if self.ladder_checker:
            random_number = random.randint(1, 6)
            self.pos += max(0, random_number - self.dropped_steps)
            if self.board.position_adjustment(self.pos) > 0:
                self.ladder_checker = True
            else:
                self.ladder_checker = False
            self.pos += self.board.position_adjustment(self.pos)
        else:
            self.pos += random.randint(1, 6)
            if self.board.position_adjustment(self.pos) > 0:
                self.ladder_checker = True
            else:
                self.ladder_checker = False
            self.pos += self.board.position_adjustment(self.pos)


class Simulation:
    def __init__(self, player_field=(Player, LazyPlayer, LazyPlayer),
                 board=Board(), seed=1337, randomize_players=True):
        self.player_field = list(player_field)
        self.board = board
        self.seed = seed
        self.randomize_players = randomize_players
        self.results = []
        """Initialise the simulation
        Parameters
        ---------
        player_field : list/tuple
            Names of the Player classes to use
        board : Board() object
            The board to use in the simulation
        seed : int
            Random generator seed
        randomize_players : Bool
            If the player_field should be shuffled before each game
        """

    def single_game(self):
        """Performs a single game and returns the winning class name and the
        number of moves

        Returns
        --------
        tuple
            tuple with winning class and number of moves
        """
        if self.randomize_players:
            random.shuffle(self.player_field)
        player_objects = [i(self.board) for i in self.player_field]
        moves = 0
        while True:
            for i in player_objects:
                i.move()
                if self.board.goal_reached(i.pos):
                    moves += 1
                    return moves, type(i).__name__
            moves += 1

    def run_simulation(self, number_of_games):
        """Runs a number of simulations and adds results to a list
        Parameters
        ----------
        number_of_games - int
            number of games to simulate
        """
        random.seed(self.seed)
        for i in range(number_of_games):
            self.results.append((self.single_game()))

    def get_results(self):
        """Returns results"""
        return self.results

    def winners_per_type(self):
        """Returns dictionary with how many wins each class had
        Return
        -------
        dict
            wins for each class
        """
        winners = [i[1] for i in self.results]
        winner_dict = {x: winners.count(x) for x in winners}
        return winner_dict

    def durations_per_type(self):
        """Returns dictionary with the number of moves that caused a win
        for every class
        Return
        -------
        dict
            moves per win for each class
        """
        winners = [i[1] for i in self.results]
        winners = list(set(winners))
        winners_dict = {}
        for i in winners:
            move_number = []
            for j in self.results:
                if j[1] == i:
                    move_number.append(j[0])
            winners_dict[i] = move_number
        return winners_dict

    def players_per_type(self):
        """Returns dictionary with the number of players of each Player class
        Return
        -------
        dict
            number of players of each class"""
        players = [type(i(self.board)).__name__ for i in self.player_field]
        player_dict = {x: players.count(x) for x in players}
        return player_dict
