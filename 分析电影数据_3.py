import pandas as pd
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
file_path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

#统计分类的列表
temp_list = df["Genre"].str.split(",").tolist() #列表嵌套列表
genre_list = list(set([i for j in temp_list for i in j]))
#构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list)
#print(zeros_df)
#给每个电影出现的位置赋值1
for i in range(df.shape[0]):
    #zeros_df.loc[0,temp_list[i]]=1
    zeros_df.loc[i,temp_list[i]] = 1

#print(zeros_df.head(3))
#统计每个分类的电影数量和
genre_count = zeros_df.sum(axis=0)
#print(genre_count)

#排序
genre_count = genre_count.sort_values()
_x = genre_count.index
_y = genre_count.values
#画图
plt.figure(figsize=(20,8),dpi=80)
plt.bar(range(len(_x)),_y)
plt.xticks(range(len(_x)),_x)
plt.show()


