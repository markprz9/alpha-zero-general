from __future__ import print_function
import sys
sys.path.append('..')
from Game import Game
import numpy as np

"""
"""

class State:
    def __init__(self):
        return [-1, -1]


class RPSGame(Game):
    def getInitBoard(self):
        return [-1, -1]

    def getBoardSize(self):
        return (2, 1)

    def getActionSize(self):
        # return number of actions
        return 3

    def getNextState(self, board, player, action):
        if action > 2:
          raise Exception("Invalid move: %d" % action)
        b = [-1, -1]
        b[0] = board[0]
        b[1] = board[1]
        if player == 1:
          b[0] = action
        if player == -1:
          b[1] = action
        return (b, -player)

    def getValidMoves(self, board, player):
        return [1]*self.getActionSize()

    def getGameEnded(self, board, player):
        if board[0] < 0 or board[1] < 0:
          return 0
        winner = 0
        # current player wins
        if (board[1] + 1) % 3 == board[0]:
          winner = 1
        # opponent wins
        if (board[0] + 1) % 3 == board[1]:
          winner = -1

        if winner != 0:
          return winner * player
        
        return 1e-4

    def getCanonicalForm(self, board, player):
        return board

    def getSymmetries(self, board, pi):
        return (board, pi)

    def stringRepresentation(self, board):
        return "[%d,%d]" % (board[0], board[1])

def display(board):
    print(board)
