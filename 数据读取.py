# import pandas as pd
# df = pd.read_csv("./dogNames2.csv")
# df_1 = pd.read_clipboard()
# print(df_1)
import  numpy as np
import pandas as pd
from matplotlib import lines
from sqlalchemy import create_engine
# 初始化数据库连接，使用pymysql模块
# MySQL的用户：root, 密码:147369, 端口：3306,数据库：test
#engine = create_engine('mysql+pymysql://81e189875e195e30:a6a2404823487464@106.53.245.88:3306/yuyue')
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/yuyue')
# 查询语句，选出employee表中的所有数据
sql = ''' select * from t_image_info; '''

# read_sql_query的两个参数: sql语句， 数据库连接
df = pd.read_sql_query(sql, engine)
# 输出employee表的查询结果
dfs = pd.DataFrame(df)

#print(dfs.head())
#print(dfs.tail(2))
#print(dfs.info())
#print(dfs.describe())统计数字类型
#print(dfs[6:20])
#print(dfs[:20]["image_cate_code"])
#通过标签索引获取数据
#dfs = dfs.loc[20,"image_id"]
#dfs = dfs.loc[20,["image_id","image_url"]]
#dfs = dfs.loc[[0,3],["image_id","image_url"]]
#选择冒号后面的数据
#dfs = dfs.loc[5:,["image_id","image_url"]]
#dfs = dfs.loc[3:6,["image_id","image_url"]]
#pandas之iloc
#dfs = dfs.iloc[1:3,[0,1,2]]
#dfs.loc[0,"image_id"]=100 赋值
#dfs = dfs.iloc[1:3,1:3]
#pandas之布尔索引
#dfs = dfs[dfs["is_deleted"]==0]
#切割
#dfs = dfs["image_url"].str.split(".").tolist()
#缺失数据处理
# dfs = pd.isnull(dfs)
# dfs = pd.notnull(dfs)

#对行进行操作
#dfs = dfs[pd.notnull(dfs["image_cate"])]
#对列进行操作
#dfs = pd.notnull(dfs[:20]["image_cate"])

#dfs = dfs.dropna(axis=0,how="all")

dfs = dfs.dropna(axis=0,how="any")
print(dfs)




# # 新建pandas中的DataFrame, 只有id,num两列
# df = pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['zhangsan', 'lisi', 'wangwu', 'zhuliu']})
# # 将新建的DataFrame储存为MySQL中的数据表，储存index列
# df.to_sql('mydf', engine, index=True)
# print('Read from and write to Mysql table successfully!')


