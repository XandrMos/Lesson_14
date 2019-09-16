# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 17:58:53 2019

@author: Xandr
"""
import random
class Life():
    def __init__(self):
        self.pole = [
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]
                ]
        self.rnd = 0
        self.history = []
    def reset(self):
        self.pole = [
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]
                ]
        self.rnd = 0
    def set(self, N):
        if not (2 <= N <= 100):
            print("Enter 2 <= N <= 100")
            return None
        self.history.append(list())
        for i in range(N):
            while True:
                 x = random.randint(0, 9)
                 y = random.randint(0, 9)
                 if self.pole[x][y] != 1:
                     self.pole[x][y] = 1
                     self.history[self.rnd].append((x,y))
                     break
        
        for i in range(10):
            for j in range(10):
                if self.pole[i][j] == 1:
                    print('*', end = "")
                else:
                    print('_', end = "")
            print()
        return None
    def count_neighbors(self, x, y):
        sum = 0
        neighbors = [(-1, -1), (-1, 0), (-1, 1), 
                    (0, -1), (0, 1), 
                    (1, -1), (1, 0), (1, 1)]
        for i in neighbors:
            n_x = x + i[0]
            n_y = y + i[1]
            if n_x == 10:
                n_x = 0
            if n_y == 10:
                n_y = 0
            if self.pole[n_x][n_y] == 1:
                sum += 1
        return sum
    def one_step(self):
        new_pole = [
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]
                ]
        for i in range(10):
            for j in range(10):
                cnt = self.count_neighbors(i, j)
                if self.pole[i][j] == 0 and cnt == 3:
                    new_pole[i][j] = 1
                elif self.pole[i][j] == 1 and cnt in (2, 3):
                    new_pole[i][j] = 1
#                elif self.pole[i][j] == 1 and cnt < 2:
#                    new_pole[i][j] = 0
#                elif self.pole[i][j] == 1 and cnt > 3:
#                    new_pole[i][j] = 0
#                else:
#                    new_pole[i][j] = new_pole[i][j]
        self.pole = new_pole
        print("Step = ", self.rnd)
        for i in range(10):
            for j in range(10):
                if self.pole[i][j] == 1:
                    print('*', end = "")
                else:
                    print('_', end = "")
            print()
        return None
    def step(self, N = 1):
        for i in range(N):
            self.one_step()
            self.rnd += 1
                    

obj = Life()
obj.set(35)
obj.step(2)

    