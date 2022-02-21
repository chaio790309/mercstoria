import pandas as pd
import geometry.realability as ra
data=pd.read_csv("unit.csv")
# print(data)


import matplotlib.pyplot as plt
filter=data["element"]=="fire" #篩選
data=data[filter]

x=range(data.shape[0]) #shape回傳[列數,行數]
name=data["name"]
y=data["atk"]
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] #讓亂碼正常顯示
plt.title("攻擊力")
plt.barh(x,y)
plt.yticks(x,name,fontsize=8)
for i in x:
    plt.text(y[i]/2, #x軸
    i-0.15, #y軸
    y[i], #文字
    fontsize=10,
    horizontalalignment='center')

plt.show()
