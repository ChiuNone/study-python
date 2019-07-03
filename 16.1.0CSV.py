#csv和json一样是一种文件格式
#将数据作为一系列以逗号分隔的值SCV写入文件

#处理锡特卡的月天气数据
#具体处理数据参见high_lows.py

#这里遇到fig.autofmt_xdate()，并没有执行。？

#涵盖更长时间:导入锡特卡的年天气数据并处理
#具体见high_lows.py

#加入最低气温
#见high_lows.py

#给图表高低气温之间着色
#见high_lows.py

#检查错误
#有时会出现故障，并未能收集到部分或者全部数据，缺失部分数据会引发异常，处理异常
#death_valley_2014.csv文件中有数据缺失，运行绘制图表代码时会报错，使用try-except-else来处理异常
#此处处理见highs_lows.py