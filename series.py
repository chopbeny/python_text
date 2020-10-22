import string

import pandas as pd
pd_1 = pd.Series([1,2,3,32,4,6])
t1 = pd.Series([1,2,3,32,4,6],index=list("judpgk"))
#字典表创建
temp_dict = {"name":"xiaohong","age":30,"tel":896566}
t3 = pd.Series(temp_dict)

t4 = {string.ascii_uppercase[i]:i for i in range(10)}
t4 = pd.Series(t4)

t5 = pd.Series(t4,index=list(string.ascii_uppercase[5:15]))



#print(list(t5.index))
#for i in t5.index:
    #print(i)
#print(t5.index)
#print(t5['F'])
#print(t5[2])
#print(t5[1,2])
#print(t5[['age','tel']])








