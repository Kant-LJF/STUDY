#!/user/bin/env python
# _*_coding=utf-8_*_
import pandas as pd
import numpy as np

# 读取股票数据
data = pd.read_csv('stock_data.csv')
data['MA_short'] = data['Close'].rolling(window=10).mean()
data['MA_long'] = data['Close'].rolling(window=30).mean()

# 计算交易信号
data['Signal'] = np.where(data['MA_short'] > data['MA_long'], 1, 0)
data['Signal'] = data['Signal'].shift(1)

# 计算账户价值
data['Position'] = data['Signal'].diff()
data['Return'] = data['Close'] * data['Position'].shift(1)
data['Account'] = (data['Return'] + 1).cumprod()

# 绘制账户价值图
import matplotlib.pyplot as plt
plt.plot(data['Account'])
plt.show()
