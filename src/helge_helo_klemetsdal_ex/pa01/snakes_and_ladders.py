# -*- coding: utf-8 -*-

__author__ = 'Helge Helo Klemetsdal', 'Anders Mølmen Høst'
__email__ = 'hegkleme@nmbu.no' 'anderhos@nmbu.no'

import random as rd
import numpy as np


def single_game(num_players):
    """
    Returns duration of single game.

    Arguments
    ---------
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : int
        Number of moves the winning player needed to reach the goal

        24	33	42	56	64	74	87
||To	5	3	30	37	27	12	70
    """

    winning_score = 90
    ladder_dict = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85}
    snake_dict = {24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}

    position_list = [0 for _ in range(num_players)]
    moves_list = [0 for _ in range(num_players)]

    while max(position_list) < winning_score:
        for index, player_position in enumerate(position_list):
            player_position += rd.randint(1, 6)
            if player_position in ladder_dict.keys():
                player_position = ladder_dict[player_position]
            if player_position in snake_dict.keys():
                player_position = snake_dict[player_position]
            position_list[index] = player_position
            moves_list[index] += 1

    winning_moves = min(moves_list)
    return winning_moves


def multiple_games(num_games, num_players):
    """
    Returns durations of a number of games.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """
    moves_and_games_list = []
    for game in range(num_games):
        moves_and_games_list.append(single_game(num_players))

    return moves_and_games_list


def multi_game_experiment(num_games, num_players, seed):
    """
    Returns durations of a number of games when playing with given seed.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game
    seed : int
        Seed used to initialise the random number generator

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """

    rd.seed(seed)
    return multiple_games(num_games, num_players)


if __name__ == "__main__":
    winning_list = multi_game_experiment(100, 4, 1)
    shortest_game = min(winning_list)
    longest_game = max(winning_list)
    median_game = np.median(winning_list)
    mean_game = np.mean(winning_list)
