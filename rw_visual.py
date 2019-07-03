import matplotlib.pyplot as plt

from random_walk import RandomWalk

#加入循环，询问是否再来一次随机漫步
while True:
    #传递参数修改默认值，增加或减少点数
    rw = RandomWalk()
    rw.fill_walk()

    #颜色映射
    points_num = list(range(rw.num_points))#映射点的先后顺序，根据顺序着色
    plt.scatter(rw.x_values, rw.y_values,
                c = points_num, cmap = plt.cm.Blues, s = 20)

    #突出起点和终点
    plt.scatter(0, 0, c = 'red', s = 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'green', s = 100)

    #调整尺寸适合屏幕大小
    plt.figure(dpi = 128, figsize=(10,6))
    #函数figure()用于指定图标的宽度和高度，分辨率，背景颜色
    #需要给figure指定参数用元组形式，指出会话窗口的尺寸大小
    #dpi= 传递分辨率大小

    plt.show()

    keep_running = input('Do you want to make anthor rw?(y/n)')
    if keep_running == 'n':
        break