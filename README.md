# SigmaGo 1.00
**SigmaGo** was inspired by **AlphaGo**. The main purpose of this repository is to experiment and learn about **Deep Reinforcement Learning**.

## 1.00
The current version of this repository is **V1.00**. At the moment the repository holds no *intelligent* Agent and is merely a shell of the Game **Go**. 

# Installation
First you will need to clone this repository into your working directory
```
$ git clone https://github.com/dmbernaal/SigmaGo.git
```
Now we will generate **hashes** which will keep track of all game_states. Otherwise (given the nature of Go) we will utilize too much memory. To do so simply run this commad first:
```
$ python generate_hashes.py > ./dlgo/zobrist.py
```
## Play Against Bot
If you want to play against the bot via Terminal simply run the following python script:
```
$ python human_v_bot.py
```
You will then be prompted to make your move! Below is the map structure of the **9x9** Go board. Simply type {LETTER}{NUMBER}. 
```python
9 . . . . . . . . .
8 . . . . . . . . .
7 . . . . . . . . .
6 . . . . . . . . .
5 . . . . . . . . .
4 . . . . . . . . .
3 . . . . . . . . .
2 . . . . . . . . .
1 . . . . . . . . .
  A B C D E F G H J
```
## Bot vs. Bot
If you simply want to watch a game of Go between two bots run the following python script:
```
$ python bot_v_bot.py
```
Both Agent's will play at *random*. For future development (Coming soon) I will include *Smart Agents* utilizing **Q-Learning** and **Policy Optimization** techniques. 

### Project Structure
```
├── README.md
├── bot_v_bot.py
├── dlgo
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── goboard.cpython-36.pyc
│   │   ├── gotypes.cpython-36.pyc
│   │   ├── utils.cpython-36.pyc
│   │   └── zobrist.cpython-36.pyc
│   ├── agent
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── base.cpython-36.pyc
│   │   │   ├── helpers.cpython-36.pyc
│   │   │   └── naive.cpython-36.pyc
│   │   ├── base.py
│   │   ├── helpers.py
│   │   └── naive.py
│   ├── goboard.py
│   ├── goboard_slow.py
│   ├── gotypes.py
│   ├── utils.py
│   └── zobrist.py
├── generate_hashes.py
└── human_v_bot.py
```
