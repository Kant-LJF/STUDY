#!/user/bin/env python
# _*_coding=utf-8_*_
 # 代码
import numpy as np
import pandas as pd

# 设置参数
# 开始日期
start_date = '2020-01-01'
# 结束日期
end_date = '2020-12-31'
# 股票代码
stock_code = '000001.SZ'

# 读取数据
data = pd.read_csv('stock_data.csv', parse_dates=[0], index_col=0)
# 选取需要的数据
data = data.loc[start_date:end_date, stock_code]

# 提取价格序列
price_sequence = np.array(data['close'])

# 建立交易模型
# 计算价格指标
# 计算最高价
max_price = np.max(price_sequence)
# 计算最低价
min_price = np.min(price_sequence)
# 计算当前价格
current_price = price_sequence[-1]

# 计算近期涨跌停状态
# 计算当前涨跌幅
change_percent = (current_price - min_price) / min_price
# 设定涨跌幅阈值
threshold = 0.1

# 定义交易信号
# 当股票涨幅超过阈值，即进行买入操作
if change_percent >= threshold:
    signal = 'Buy'
# 否则持有
else:
    signal = 'Hold'

# 打印模型结果
print('Model Result:')
print('Max Price：{}'.format(max_price))
print('Min Price：{}'.format(min_price))
print('Current Price：{}'.format(current_price))
print('Change Percent：{}'.format(change_percent))
print('Signal：{}'.format(signal))