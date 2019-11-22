# -*- coding: utf-8 -*-

"""
Set of compatibility tests for PA02.
"""

__author__ = 'Helge Helo Klemetsdal, Adam Julius Olof Kviman'
__email__ = 'hegkleme@nmbu.no, juliukvi@nmbu.no'

import chutes_simulation as cs
import pytest
import random


class TestBoard:
    """
    Tests for Board class.
    """

    def test_goal_reached(self):
        """Returns True for position >= 90 and False for position < 90"""
        b = cs.Board()
        output = b.goal_reached(91)
        assert output
        output = b.goal_reached(80)
        assert not output

    def test_position_adjustment(self):
        """Test to check that if position is on a ladder output is positive,
        if position is on a chute output is negative and if position is not on
        a ladder or chute return 0"""
        b = cs.Board()
        output = b.position_adjustment(1)  # 1 is a ladder
        assert output > 0
        output = b.position_adjustment(24)  # 24 is a chute
        assert output < 0
        output = b.position_adjustment(2)  # 2 is not a ladder or chute
        assert output == 0

    def test_position_adjusetment_steps(self):
        """Test to see that the output is the correct amount of steps to adjust
        """
        b = cs.Board()
        output = b.position_adjustment(1)  # ladder goes from 1 to 40
        assert output == 39
        output = b.position_adjustment(24)  # chute goes from 24 to 5
        assert output == -19
        output = b.position_adjustment(2)  # not a ladder or chute
        assert output == 0


class TestPlayer:
    """
    Tests for Player class.
    """

    def test_move_start(self):
        """Test that the move method works in the start. Since we start at
         position zero the new position should be any of these numbers
          (2, 3, 4, 5, 6, 40)"""
        new_pos = []
        expected_positions = [2, 3, 4, 5, 6, 40]
        conditional = True
        for i in range(20):
            b = cs.Player()
            b.move()
            new_pos.append(b.pos)
        for j in new_pos:
            if j not in expected_positions:
                conditional = False
        assert conditional

    def test_move(self):
        """Test that the move method works when not being in the
        start position, if we start on position 9 the new position should be
        any of these numbers (10, 11, 12, 13, 14, 15)"""
        new_pos = []
        expected_positions = [10, 11, 12, 13, 14, 15]
        conditional = True
        for i in range(20):
            b = cs.Player()
            b.pos = 9
            b.move()
            new_pos.append(b.pos)
        for j in new_pos:
            if j not in expected_positions:
                conditional = False
        assert conditional


class TestResilientPlayer:

    def test_move(self):
        """Test to see if the chutes_checker conditional is True after stepping
        on a chute"""
        b = cs.Board()
        p = cs.ResilientPlayer(b)
        random.seed(1)
        p.pos = 22  # We set seed to 1 and position to 22 to make sure the move
        # method take the ResilientPlayer to 24 which is a chute
        p.move()
        assert p.chutes_checker

    def test_move_steps(self):
        """Test to see that the ResilientPlayer takes an extra step after
        going down a chute"""
        b = cs.Board()
        p = cs.ResilientPlayer(b)
        random.seed(1)
        p.pos = 22  # We set seed to 1 and position to 22 to make sure the move
        # method take the ResilientPlayer to 24 which is a chute
        p.move()   # Moves the ResilientPlayer to 5
        random.seed(2)  # Reset seed so that the next move will be 1 step plus
        # the extra step which will take the ResilientPlayer to
        # position 7
        p.move()
        assert p.pos == 7


class TestLazyPlayer:
    def test_move(self):
        """Test to see if the ladder conditional is True after stepping
        on a ladder"""
        b = cs.Board()
        p = cs.LazyPlayer(b)
        random.seed(1)
        p.pos = 6  # We set seed to 1 and position to 6 to make sure the move
        # method take the LazyPlayer to 8 which is a ladder
        p.move()
        assert p.ladder_checker

    def test_move_lazy(self):
        """Test to see that the LazyPlayer takes one less step after going up
        a ladder"""
        b = cs.Board()
        p = cs.LazyPlayer(b)
        random.seed(1)
        p.pos = 6  # We set seed to 1 and position to 6 to make sure the move
        # method take the LazyPlayer to 8 which is a ladder
        p.move()  # Moves the LazyPlayer to 10
        random.seed(1)  # Reset seed so that the next move takes the LazyPlayer
        # to position 11 (It would go to 12 if it was not Lazy)
        p.move()
        assert p.pos == 11

    def test_move_backwards(self):
        """Test to see that the LazyPlayer can not move backwards if
        dropped_steps is more than 1"""
        b = cs.Board()
        p = cs.LazyPlayer(b, dropped_steps=3)
        random.seed(1)
        p.pos = 6  # We set seed to 1 and position to 6 to make sure the move
        # method take the LazyPlayer to 8 which is a ladder
        p.move()  # Moves the LazyPlayer to 10
        random.seed(1)  # Reset seed so that the next move takes the LazyPlayer
        # to position 10 (It would go to 12 if it was not Lazy
        # and if it could go backwards it would go to pos 9)
        p.move()
        assert p.pos == 10


class TestSimulation:
    """Tests for Simulation class."""

    def test_single_game(self):
        """single_game() returns non-negative integer and class name"""
        s = cs.Simulation([cs.Player, cs.Player])
        nos, wc = s.single_game()
        assert nos > 0
        assert type(nos) == int
        assert wc == 'Player'

    def test_single_game_randomize_players(self):
        """If Simulation object has randomize_players argument then
        player_field should be shuffled"""
        s = cs.Simulation([cs.Player, cs.LazyPlayer, cs.ResilientPlayer],
                          randomize_players=True)
        for i in range(1):
            current_player_field = list(s.player_field)
            s.single_game()
            assert current_player_field != s.player_field

    def test_run_simulation(self):
        """run_simulation() can be called and runs the correct
        amount of games"""
        s = cs.Simulation()
        s.run_simulation(6)
        assert len(s.results) == 6

    def test_average_winner(self):
        """Test that the ResilientPlayer takes less steps than the Player and
        that the Player takes less steps than the LazyPlayer on average"""
        s = cs.Simulation([cs.Player, cs.LazyPlayer, cs.ResilientPlayer],
                          randomize_players=True)
        s.run_simulation(6000)
        winner_dict = s.winners_per_type()
        listoftuples = sorted(winner_dict.items(), reverse=True, key=lambda x: x[1])
        print(winner_dict)
        print(listoftuples)
        assert listoftuples[0][0] == "ResilientPlayer"
        assert listoftuples[1][0] == "Player"
        assert listoftuples[2][0] == "LazyPlayer"
