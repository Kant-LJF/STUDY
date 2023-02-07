#!/user/bin/env python
# _*_coding=utf-8_*_
import pandas as pd
import numpy as np


def turtle_strategy(df):
    # 计算 20 日最高价与最低价
    df['20_day_high'] = df['close'].rolling(window=20).max()
    df['20_day_low'] = df['close'].rolling(window=20).min()

    # 计算 N 仓位
    N = int(df['close'].mean() / df['20_day_high'].mean())

    # 计算 N 天的最高价与最低价
    df['N_day_high'] = df['close'].rolling(window=N).max()
    df['N_day_low'] = df['close'].rolling(window=N).min()

    # 计算开仓价格
    df['long_entry'] = df['N_day_high'] + (df['20_day_high'] - df['20_day_low']) * 0.5
    df['short_entry'] = df['N_day_low'] - (df['20_day_high'] - df['20_day_low']) * 0.5

    # 初始仓位
    df['position'] = np.nan
    df.loc[df['close'] > df['long_entry'], 'position'] = 1
    df.loc[df['close'] < df['short_entry'], 'position'] = -1

    # 计算持仓价格
    df['hold_price'] = np.nan
    df.loc[df['position'] == 1, 'hold_price'] = df['long_entry']
    df.loc[df['position'] == -1, 'hold_price'] = df['short_entry']

    return df
