import pandas as pd
import geometry.realability as ra
data=pd.read_csv("unit.csv")
# print(data)

while True:
    enemyelement=input("輸入敵人屬性 (fire / water / wind / light / dark) : ")
    if enemyelement in ["fire","water","wind","light","dark"]:
        match enemyelement:
            case "fire":
                element ="water"
            case "water":
                element ="wind"
            case "wind":
                element ="fire"
            case "light":
                element ="dark"
            case "dark":
                element ="light"
        break
    else:
        print("無效的輸入")
        continue

while True:
    enemytraget=input("輸入敵人部位數 (2 / 3 / 4 / 5) : ")
    if enemytraget in ["2","3","4","5"]:
        traget=enemytraget
        break
    else:
        print("無效的輸入")
        continue

while True:
    bonus=input("輸入加成武器編號 (1.弓矢 2.魔法 3.銃弾 4.純比較) : ")
    if bonus in ["1","2","3","4"]:
        match bonus:
            case "1":
                bonus="Bow"
                bonus2="弓矢"
            case "2":
                bonus="Magic"
                bonus2="魔法"
            case "3":
                bonus="Gun"
                bonus2="銃弾"
            case "4":
                bonus2="無"
        break
    else:
        print("無效的輸入")
        continue

while True:
    time=input("輸入預期時間 (建議25左右) : ")
    if time.isdigit():
        break
    else:
        print("無效的輸入")
        continue

print("敵人屬性:",enemyelement," 部位數:",traget," 加成武器:",bonus2," 預期時間:",time+"秒")







import matplotlib.pyplot as plt
filter=data["element"]==element #篩選對應屬性
data=data[filter]
index=data.index.tolist() #取索引供取資料

#進場攻速
data["ratks"]=ra.atks(data["atks"])

#實際體數
data["rtraget"]=ra.traget(data["traget"],traget,index)

#集球速度
data["rballsec"]=ra.ballsec(data["traget"],data["hit"],data["ratks"],data["rtraget"])

#一輪時間
data["round"]=ra.rround(data["traget"],data["rballsec"],data["ratks"])

#進場攻擊
data["ratk"]=ra.atk(data["atk"],data["growth"])

#普攻期望


#技能期望 判斷武器算法


#進場補正
if element in ["fire","water","wind"]:
    data["rele"]=ra.elefww(data[enemyelement])
else:
    data["rele"]=ra.eleld(data[enemyelement])

x=range(data.shape[0]) #shape回傳[列數,行數] 取得總列
name=data["name"]
y=data["ratk"]
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] #讓亂碼正常顯示
plt.title("測試用")
plt.barh(x,y)
plt.yticks(x,name,fontsize=8)
for i in index:
    plt.text(
    int(y[i])/2, #x軸
    i-index[0], #y軸
    y[i], #文字
    fontsize=10,
    verticalalignment="center",
    horizontalalignment="center")

plt.show()
