from dlgo import agent
from dlgo import goboard
from dlgo import gotypes
from dlgo.utils import print_board, print_move
import time


def main():
  board_size = 9 # we will play 9x9 for now
  game = goboard.GameState.new_game(board_size)
  bots = {
    gotypes.Player.black: agent.naive.RandomBot(),
    gotypes.Player.white: agent.naive.RandomBot()
  }

  while not game.is_over():
    time.sleep(0.1) # 300 milisecond delay, so we can observe the game
    print(chr(27) + "[2J") # clearing the screen after every move, so it doesn't spam the terminal
    print_board(game.board)
    bot_move = bots[game.next_player].select_move(game)
    game = game.apply_move(bot_move)
    print_move(game.next_player, bot_move)



if __name__ == '__main__':
  main()