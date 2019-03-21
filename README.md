# SigmaGo 1.00
**SigmaGo** was inspired by **AlphaGo**. The main purpose of this repository is to experiment and learn about **Deep Reinforcement Learning**.

## 1.00
The current version of this repository is **V1.00**. At the moment the repository holds no *intelligent* Agent and is merely a shell of the Game **Go**. 

If you are to run: 
```
$ python bot_v_bot.py
```

Both Agent's will play at *random*. For future development (Coming soon) I will include *Smart Agents* utilizing **Q-Learning** and **Policy Optimization** techniques. 

## Install
To run this repository simple run:
```
$ git clone https://github.com/dmbernaal/SigmaGo.git
```

To copy into your working directy. Then simply run ```$ python bot_v_bot.py```

### Project Structure
```
├── README.md
├── bot_v_bot.py
└── dlgo
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-36.pyc
    │   ├── goboard.cpython-36.pyc
    │   ├── gotypes.cpython-36.pyc
    │   └── utils.cpython-36.pyc
    ├── agent
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-36.pyc
    │   │   ├── base.cpython-36.pyc
    │   │   ├── helpers.cpython-36.pyc
    │   │   └── naive.cpython-36.pyc
    │   ├── base.py
    │   ├── helpers.py
    │   └── naive.py
    ├── goboard.py
    ├── goboard_slow.py
    ├── gotypes.py
    └── utils.py
```