from random import randint

class Die():
    '''表示一个骰子的类'''
    def __init__(self, num_sides = 6):
        '''默认6面骰子'''
        self.num_sides = num_sides

    #定义一个方法，随机掷一次
    def roll(self):
        return randint(1, self.num_sides)