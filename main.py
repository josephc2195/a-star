import numpy as np
from numpy import random as ra

class Star:
        def __init__(self):

                board = np.empty((15, 15), dtype=object)

                blocked = False
                for i in range(15):
                        for x in range(15):
                                ten = ra.randint(1, 10)
                                if ten != 1:
                                        board[i][x] = 0
                                else:
                                        board[i][x] = 1
                self.startRow, self.startCol = self.getStart()
                self.goalRow, self.goalCol = self.getGoal()
                openList = [(self.startRow, self.startCol)]
                
        def getStart(self):
                row = input("Enter the row you want the starting node to be on: ")
                col = input("Enter the column you want the starting node to be on: ")
                startCoords = (row, col)
                return startCoords

        def getGoal(self):
                row = input("Enter the row you want the goal node to be on: ")
                col = input("Enter the column you want the goal node to be on: ")
                goalCoords = (row, col)
                return goalCoords

