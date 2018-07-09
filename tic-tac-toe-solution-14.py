#!/usr/bin/env python3
# This special version of Tic-Tac-Toe is defined
# - for any grid size Cbetween 3 and 20
# - for 2 to 20 players
# If you set a size of 3 and 2 players, you get the standard Tic-Tac-Toe game

import re
from collections import namedtuple
from random import randint
from time import sleep

Move = namedtuple('Move', 'x y')

class Player:
    """Generic definition of a player, to be subclassed"""

    def __init__(self, name):
        self.name = name

    def next_move(self, game):
        pass

class Game:
    """A Tic-Tac-Toe game on a grid of any size"""

    def __init__(self, players, size=3):
        self.players = players
        self.grid = [ [' ']*size for i in range(size) ]
        self.moves = [] # history
        self.finished = False

    # build a pretty string representation of the state
    def __str__(self):
        sep = "+---"*self.size + "+"
        mask = "| {} "*self.size + "|"
        lines = [sep]
        for row in self.grid:
            lines.append(mask.format(*row))
            lines.append(sep)
        return "\n".join(lines)

    @property
    def size(self):
        return len(self.grid)

    @property
    def current_player(self):
        if self.finished:
            return None
        return self.players[len(self.moves)%len(self.players)]

    def is_valid(self, move):
        size = self.size
        return (0 <= move.x <= size) and (0 <= move.y <= size) and (self.grid[move.y][move.x]==" ")

    # move must be valid
    def apply(self, move):
        player = self.current_player
        if self.is_winning_move(move):
            print("Player {} wins!".format(player.name))
            self.finished = True
        self.grid[move.y][move.x] = player.name
        self.moves.append(move)
        size = self.size
        if not self.finished and len(self.moves)==size*size:
            print("No winner!")
            self.finished = True

    # in a generalized grid of any size we define a winning move by one which
    # completes an horizontal or medial line or one of the two diagonals
    def is_winning_move(self, move, name = None):
        if name is None:
            name = self.current_player.name
        size = self.size
        if all(self.grid[y][move.x]==name or y==move.y for y in range(size)):
            return True # whole column
        if all(self.grid[move.y][x]==name or x==move.x for x in range(size)):
            return True # whole row
        if move.x==move.y:
            if all(self.grid[x][x]==name or x==move.x for x in range(size)):
                return True # first diagonal
        if move.x==size-move.y-1:
            if all(self.grid[size-x-1][x]==name or x==move.x for x in range(size)):
                return True # second diagonal
        return False

    # ask the current player for a position and returns it
    # ask again until the position is valid
    def play_one_move(self):
        if self.current_player is None:
            return # game is finished. We can't play
        while True:
            move = self.current_player.next_move(self)
            if self.is_valid(move):
                self.apply(move)
                return
            print("Invalid position!")

    def play_whole(self):
        while not self.finished:
            self.play_one_move()
            print(self)

    def replay(self, delay=1.3):
        game = Game(self.players, self.size)
        print(game)
        for move in self.moves:
            sleep(delay)
            game.apply(move)
            print(game)

class CliPlayer(Player):
    """A player implemented by asking the position with a CLI invite"""

    def next_move(self, game):
        str = input("Type a position:\n").strip()
        t = re.findall(r'\d+', str)
        if len(t)<2:
            print("we need two numbers!")
            return self.next_move(game)
        return Move(int(t[0]), int(t[1]))

class SimpleAI(Player):
    """An automatic player checking what moves are winning"""

    def next_move(self, game):
        size = game.size
        if len(game.moves)==0 and size%2==1:
            return Move(size//2, size//2)
        valid_moves = [ Move(x, y) for x in range(size) for y in range(size) if game.grid[y][x]==' ' ]
        for move in valid_moves:
            if (game.is_winning_move(move, self.name)):
                return move
        for player in game.players:
            if player is self:
                continue
            for move in valid_moves:
                if (game.is_winning_move(move, player.name)):
                    return move
        return valid_moves[randint(0, len(valid_moves)-1)]

def main():
    while True:
        size = int(input("Please give the grid size:\n"))
        if size<3:
            print("This is too small!")
        elif size>20:
            print("This is too big!")
        else:
            break
    nb_players = int(input("Give the number of players (hit enter for just 2 players):\n"))
    if not (1 < nb_players < 20):
        nb_players = 2
    if nb_players==2:
        names = ["X", "O"]
    else:
        names = [ chr(n+65) for n in range(nb_players) ]
    players = [ SimpleAI(name) for name in names[:-1] ] + [ CliPlayer(names[-1]) ]
    print("Players are", ",".join(names))
    print("You're Player", names[-1])
    game = Game(players, size)
    game.play_whole()
    want_replay = input("Do you want to see a game replay [Y|n] ?\n")
    if want_replay is not "n":
        print("Game replay:")
        game.replay()

main()

