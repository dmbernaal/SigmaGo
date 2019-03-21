import numpy as np
import copy
from dlgo.gotypes import Player

class Move():
  """
  Any action a player can take: is_play, is_pass, is_resign:

      is_play: placing a stone
      is_pass: passing turn
      is_resign: resigning from game
  """
  def __init__(self, point=None, is_pass=False, is_resign=False):
    assert (point is not None) ^ is_pass ^ is_resign
    self.point = point
    self.is_play = (self.point is not None)
    self.is_pass = is_pass
    self.is_resign = is_resign

  @classmethod
  def play(cls, point):
    """This move places a stone on the board"""
    return Move(point=point)

  @classmethod
  def pass_turn(cls):
    """This move passes"""
    return Move(is_pass=True)

  @classmethod
  def resign(cls):
    """This move resigns the current game"""
    return Move(is_resign=True)


class GoString():
  """All stones & liberties will be stored as units to decrease computational expense
  
    Go String are a chain of connected stones of the same color  
  """
  def __init__(self, color, stones, liberties):
    self.color = color
    self.stones = set(stones) # builds string of 'stones'
    self.liberties = set(liberties) # builds string of 'liberties'

  def remove_liberty(self, point):
    self.liberties.remove(point)

  def add_liberty(self, point):
    self.liberties.add(point)

  def merged_with(self, go_string):
    """Returns a new Go string containing all stones in both strings"""
    assert go_string.color == self.color 
    combined_stones = self.stones | go_string.stones
    return GoString(self.color, combined_stones, (self.liberties | go_string.liberties) - combined_stones)

  @property
  def num_liberties(self):
    return len(self.liberties)

  def __eq__(self, other):
    return isinstance(other, GoString) and \
      self.color == other.color and \
      self.stones == other.stones and \
      self.liberties == other.liberties
  

class Board():
  """A board is initialized as an empty grid with a specialized number of rows and cols"""
  def __init__(self, num_rows, num_cols):
    self.num_rows = num_rows
    self.num_cols = num_cols
    self._grid = {} # Keeps track of Go Board internally

  def place_stone(self, player, point):
    """
    We will first check whether the point is within bounds for a given board and that the point
    hasn't been played yet - calling:
      is_on_grid(), 
      get(), 
      get_go_string()
    """
    assert self.is_on_grid(point) # checking if point is on grid
    assert self._grid.get(point) is None # checking if this point is occupied

    # for that point we will count all neighbors that are: same color, opposite color, liberties
    adjacent_same_color = []
    adjacent_opposite_color = []
    liberties = []

    for neighbor in point.neighbors(): # grabbing all neighbors for that point
    """Examining direct neighbors of this point"""

      if not self.is_on_grid(neighbor):
        # neighbor isn't on the grid = continue (check the next neighbor)
        continue
      neighbor_string = self._grid.get(neighbor) # get neighbor on board (check dicitonary)

      if neighbor_string is None:
        # if neighbor doesnt exist, it is a liberty - add the liberty
        liberties.append(neighbor)

      # adding adjacent same colors
      elif neighbor_string.color == player:
        if neighbor_string not in adjacent_same_color:
          adjacent_same_color.append(neighbor_string)

      # adding adjacent opposite colors
      else:
        if neighbor_string not in adjacent_opposite_color:
          adjacent_opposite_color.append(neighbor_string)

    new_string = GoString(player, [point], liberties)

    for same_color_string in adjacent_same_color:
      """Merge any adjacent strings of the same color"""
      new_string = new_string.merged_with(same_color_string)
    for new_string_point in new_string.stones:
      self._grid[new_string_point] = new_string

    for other_color_string in adjacent_opposite_color:
      """Reduce liberties of any adjacent strings of the opposite color"""
      other_color_string.remove_liberty(point)

    for other_color_string in adjacent_opposite_color:
      """If any opposite-color strings now have zero liberties, remove them"""
      if other_color_string.num_liberties == 0:
        self._remove_string(other_color_string)

    def _remove_string(self, string):
      for point in string.stones:
        for neighbor in point.neighbors():
          """Removing a string can create liberties for other strings"""
          neighbor_string = self._grid.get(neighbor)
          if neighbor_string is None:
            continue
          if neighbor_string is not string:
            neighbor_string.add_liberty(point)
        self._grid[point] = None

  def is_on_grid(self, point):
    """Checking if point is on the board"""
    return 1 <= point.row <= self.num_rows and \
    1 <= point.col <= self.num_cols
          
  def get(self, point):
    """Returns the content of a point on the board: a Player if a stone is on taht point, or else None"""
    string = self._grid.get(point)
    if string is None:
      # otherwise, not taken
      return None
    return string.color # else, return that string color

  def get_go_string(self, point):
    """Returns the entire string of stones at a point: a GoString if a stone is on that point, or else None"""
    string = self._grid.get(point)
    if string is None:
      return None
    return string


class GameState():
  def __init__(self, board, next_player, previous, move):
    self.board = board
    self.next_player = next_player
    self.previous_state = previous
    self.last_move = move

  def apply_move(self, move):
    """Returns a new GameState after applying a move"""
    if move.is_play:
      next_board = copy.deepcopy(self.board)
      next_board.place_stone(self.next_player, move.point)
    else:
      next_board = self.board
    return GameState(next_board, self.next_player.other, self, move)

  def is_over(self):
    if self.last_move == None:
      return False
    if self.last_move.is_resign:
      return True
    second_last_move = self.previous_state.last_move
    if second_last_move is None:
      return False
    return self.last_move.is_pass and second_last_move.is_pass

  def is_move_self_capture(self, player, move):
    if not move.is_play:
      return False
    next_board = copy.deepcopy(self.board)
    next_board.place_stone(player, move.point)
    new_string = next_board.get_go_string(move.point)
    return new_string.num_liberties == 0

  @classmethod
  def new_game(cls, board_size):
    if isinstance(board_size, int):
      board_size = (board_size, board_size)
      board = Board(*board_size)
      return GameState(board, player.black, None, None)

  @property
  def situation(self):
    return (self.next_player, self.board)

  def does_move_violate_ko(self, player, move):
    if not move.is_play:
      return False
    next_board = copy.deepcopy(self.board)
    next_board.place_stone(player, move.point)
    next_situation = (player.other, next_board)
    past_state = self.previous_state
    while past_state is not None:
      if past_state.situation == next_situation:
        return True
      past_state = past_state.previous_state
    return False

  def is_valid_move(self, move):
    if self.is_over():
      return False
    if move.is_pass or move.is_resign:
      return True
    return (self.board.get(move.point) is None and not self.is_move_self_capture(self.next_player, move) and not self.does_move_violate_ko(self.next_player, move))
