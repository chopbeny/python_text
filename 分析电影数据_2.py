import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file_path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

#获取平均评分
#df = df["Rating"].mean()

#导演的人数
#df = len(set(df["Director"].tolist()))
#df = len(df["Director"].unique()) #unique获取的数据变成列表

#获取演员的人数
temp_actors_list = df["Actors"].str.split(",").tolist()
actors_list = [i for j in temp_actors_list for i in j]
actors_num = len(set(actors_list))

print(actors_num)


