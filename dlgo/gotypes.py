import enum
from collections import namedtuple

class Player(enum.Enum):
  """A player is either white or black stone"""

  black = 1
  white = 2

  @property # getter
  def other(self):
    return Player.black if self == Player.white else Player.white


class Point(namedtuple('Point', 'row col')):
  """
     Used to represents coordinated on the board
     Allows us to access the coordinates as point.row and point.col instead of point[0] point[1]
  """

  def neighbors(self):
    return [
      Point(self.row - 1, self.col),
      Point(self.row + 1, self.col),
      Point(self.row, self.col -1),
      Point(self.row, self.col +1)
    ]