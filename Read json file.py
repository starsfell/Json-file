# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 16:15:00 2018

@author: xintong.yan
"""

import pandas as pd
import json

# 读取只包含一个json对象文件的txt
path = 'C:/Users/xintong.yan/Desktop/data2.txt'
file = open(path,'r')
js = file.read()

data_list = json.loads(js)
data_df = pd.DataFrame(data_list,index = [0])


# 读取含有所有行的txt文件
# 读取json中的各个行
path = 'C:/Users/xintong.yan/Desktop/data.txt'
file = open(path,'rb')

js = file.read().decode('utf-8')
type(js)

df_empty = pd.DataFrame()

for line in open(path, encoding='UTF-8'): 
    data_list = json.loads(line)                 # 读取每一行，将每一行读取成为json文件
    data_df = pd.DataFrame(data_list, index=[0]) # 将每一行转成data frame的形式
    df_empty = df_empty.append(data_df)          # 将每一行转化append添加到原来空的data frame下
















