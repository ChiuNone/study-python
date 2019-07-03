from random import choice
'''choice随机选'''

class RandomWalk():
    '''一个生成随机漫步数据的类'''
    def __init__(self, num_points = 5000):
        '''初始化属性，默认点数5000'''
        self.num_points = num_points
        '''所有漫步始于坐标（0，0）'''
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''计算所有随机漫步的点'''

        #不断地随机漫步，直到小于5000点
        while len(self.x_values) < self.num_points:
        # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([-1, 1])#选择向左还是向右
            x_distance = choice([0, 1, 2, 3, 4])#选择每次走多少
            x_step = x_direction * x_distance#x走的结果

            y_direction = choice([-1, 1])#选在向上还是向下
            y_distance = choice([0, 1, 2, 3, 4, 5])
            y_step = y_direction * y_distance

            #拒绝原地踏步
            if x_step and y_step == 0:
                continue

            #计算下一个坐标
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)