import pandas as pd
df = pd.read_csv("./dogNames2.csv")
df = pd.DataFrame(df)
#print(df.head())
#print(df.info())

#dataFrame中的排序方法
df = df.sort_values(by="Count_AnimalName",ascending=False)
#print(df.head(5))
#方括号写数字表示对行进行操作
#写字符串，表示去列索引，对列进行操作
#print(df[:20])
#print(df[:20]["Row_Labels"])

df = df[(df["Row_Labels"].str.len()>4) & (df["Count_AnimalName"]>700)]
print(df)







