#重构方法fill_walk()
from random import choice

class RandomWalk():
    def __init__(self, points_num = 5000):
        self.points_num = points_num
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([-1, 1])
        distance = choice(list(range(9)))
        step = direction * distance
        return step

    def fill_walk(self):
        while len(self.x_values) < self.points_num:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step and y_step == 0:
                break

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

