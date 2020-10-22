import pandas as pd
import numpy as np
t1 = pd.DataFrame(np.arange(12).reshape(3,4))

t2 = pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("wxyz"))

t3 = {"name":["xiaoming","xiaohong"],"age":[20,56],"tel":[85263,789612]}
t3 = pd.DataFrame(t3)


print(t3)




