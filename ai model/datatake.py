#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 8:27
# @Author  : zhikeyang
# @Email   : 15221141663@163.com

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import re
from keras.models import Sequential

from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout, Activation
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error


def deal_data(data, timesteps, predict_size, cols):
    from sklearn.preprocessing import StandardScaler
    df = series_to_supervised(data, n_in=timesteps, n_out=predict_size, dropnan=True)
    df_scale = pd.DataFrame(StandardScaler().fit_transform(df.values), columns=df.columns)
    trainx, trainy = df_scale.iloc[:, :-predict_size * cols], df_scale.iloc[:, -predict_size * cols:]
    print(trainx.shape)
    trainx = np.reshape(np.ravel(trainx), (trainx.shape[0], timesteps1, -1))
    return trainx, trainy


def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    """
    Frame a time series as a supervised learning dataset.
    Arguments:
        data: Sequence of observations as a list or NumPy array.
        n_in: Number of lag observations as input (X).
        n_out: Number of observations as output (y).
        dropnan: Boolean whether or not to drop rows with NaN values.
    Returns:
        Pandas DataFrame of series framed for supervised learning.
    """
    n_vars = 1 if type(data) is list else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j + 1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j + 1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j + 1, i)) for j in range(n_vars)]
    # put it all together
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)

    return agg


dataset = pd.read_csv('F:/DATASET/datanew_5min/HZW/df_20_5MIN_AD.csv')
dataset['datetime'] = pd.to_datetime(dataset['datetime'])
dataset.set_index("datetime", inplace=True)
df = dataset[dataset['PLC6_KQFT_20202_val'] > 0]

df1 = df[
    ['CS_AD', 'DO20202G', 'DO20203G', 'JS_AD', 'PLC6_WNFT_20203_val', 'PLC6_JSFT_20203_val', 'PLC6_KQFT_20202_val']]
timesteps = 6
predict_size = 1
df1_new = series_to_supervised(df1, n_in=timesteps, n_out=predict_size, dropnan=True)
df1_new.head()
varLS = []
cols = list(df1_new.columns)
for j in range(1, 8):
    pattern = re.compile(r'^var{}(\S*)'.format(j))

    varLS.append([(pattern.match(i)).group(0) for i in cols if pattern.match(i) != None])
for i in range(1, len(varLS) + 1):
    s = 'var{}_'.format(i)

    df1_new[s + 'max'] = df1_new[varLS[i - 1]].max(axis=1)
    df1_new[s + 'min'] = df1_new[varLS[i - 1]].min(axis=1)
    df1_new[s + 'mean'] = df1_new[varLS[i - 1]].mean(axis=1)

df_new1 = df1_new.loc[:, 'var1_mean':'var7_min']
dataset = pd.concat([df_new1, df1], axis=1).iloc[timesteps:, :]
timesteps1 = 72
predict_size1 = 24
df_new2 = series_to_supervised(dataset, n_in=timesteps1, n_out=predict_size1, dropnan=True)
df_new2.head()
df_scale = pd.DataFrame(StandardScaler().fit_transform(df_new2.values), columns=df_new2.columns)
timesteps1 = 72
predict_size1 = 24
cols = dataset.shape[1]
trainx, trainy = deal_data(df_scale, timesteps1, predict_size1, cols)
trainx = np.reshape(np.array(trainx), (trainx.shape[0], timesteps1, -1))


def trainModel(train_X, train_Y):
    '''
    trainX，trainY: 训练LSTM模型所需要的数据
    '''
    model = Sequential()
    model.add(LSTM(144, input_shape=(timesteps1, cols), return_sequences=True))
    model.add(Dropout(0.3))
    # model.add(Dropout(0.3))
    model.add(LSTM(288, return_sequences=True))
    model.add(Dropout(0.5))
    model.add(LSTM(576, return_sequences=True))
    model.add(Dropout(0.5))
    model.add(LSTM(288, return_sequences=True))
    model.add(Dropout(0.3))
    model.add(LSTM(144, return_sequences=False))
    # model.add(Dropout(0.2))
    model.add(Dense(train_Y.shape[1]))
    model.compile(loss="mean_squared_error", optimizer="adam")
    model.fit(train_X, train_Y, epochs=30, batch_size=600)
    model.save('F:/MODEL/20200525air.h5')

    return model



if __name__ == '__main__':
    trainModel(trainx, trainy.values)