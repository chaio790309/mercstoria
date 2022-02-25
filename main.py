import pandas as pd
import geometry.realability as ra
import geometry.allunit as ga
import geometry.unittable as gu
import os


print("檢查更新中...")
result=os.path.isfile("unit.csv") #確認檔案

if result:
    data=pd.read_csv("unit.csv")    
    unitcount=ga.check() #確認數量
    if unitcount != data.shape[0]:
        update=input("偵測到新資料，是否進行更新 (y/n) : ")
        while True:
            match update:
                case "y":
                    gu.unittable()
                    data=pd.read_csv("unit.csv")
                    break
                case "n":
                    break
                case _:
                    print("無效的輸入")
                    continue
    else:
        print("資料不須更新")
else:
    print("未存在檔案，將進行資料更新")
    gu.unittable()
    data=pd.read_csv("unit.csv")
# print(data)


#輸入參數
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
# element,enemyelement ="water","fire"
while True:
    enemytraget=input("輸入敵人部位數 (2 / 3 / 4 / 5) : ")
    if enemytraget in ["2","3","4","5"]:
        traget=enemytraget
        break
    else:
        print("無效的輸入")
        continue
# traget=3
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
# bonus,bonus2="Gun","銃弾"
while True:
    time=input("輸入預期時間 (建議25左右) : ")
    if time.isdigit():
        break
    else:
        print("無效的輸入")
        continue
# time="25"
print("敵人屬性:",enemyelement," 部位數:",traget," 加成武器:",bonus2," 預期時間:",time+"秒")







import matplotlib.pyplot as plt
filter=data["element"]==element #篩選對應屬性
data=data[filter]


# 加成武器
bonusweapon=[]
for w in data["weapon"]:
    if w == bonus:
        if w == "Bow":
            bonusweapon+=[1.35*1.175]
        else:
            bonusweapon+=[1.35]
    else:
        if w == "Bow":
            bonusweapon+=[1.175]
        else:
            bonusweapon+=[1]
data["bonus"]=bonusweapon

#進場攻速
data["ratks"]=ra.atks(data["atks"])

#實際體數
data["rtraget"]=data["traget"]
data["rtraget"]=ra.traget(data["rtraget"],traget,data.index)

#集球速度
data["rballsec"]=ra.ballsec(data["traget"],data["hit"],data["ratks"],data["rtraget"])

#一輪時間
data["round"]=ra.rround(data["traget"],data["rballsec"],data["ratks"])

#進場攻擊
data["ratk"]=ra.atk(data["atk"],data["growth"])

#滿寵補正
data["relement"]=ra.element(data["element"],data[enemyelement],data.index)

#普攻期望
data["normalDPS"]=ra.normalDPS(data["rtraget"],data["ratks"],data["ratk"],data["relement"],data["bonus"])


#技能期望 判斷武器算法
data["skillDPS"]=data["weapon"]
data["skillDPS"]=ra.SkillDPS(data["skillDPS"],data["traget"],data["hit"],data["relement"],data["ratk"],data.index,time,data["bonus"])

#發動1期望
data["skill1"]=ra.skill1(data["round"],data["traget"],data["rballsec"])

#發動2期望
data["skill2"]=ra.skill2(data["round"],data["traget"],data["rballsec"])

#發動期望次數
data["skillnumber"]=data["skill2"]
data["skillnumber"]=ra.skillnumber(data["skillnumber"],time,data.index)

#排序用期望傷害
data["expectedDPS"]=ra.expectedDPS(data["normalDPS"],data["skillDPS"],data["skillnumber"])

#排序並重置索引
data=data.sort_values(by=["expectedDPS"],ascending=True).reset_index(drop=True)
# index=data.index.tolist() #取索引供取資料


x=range(data.shape[0]) #shape回傳[列數,行數] 取得總列
name=data["name"]
y=data["normalDPS"] #測試值
z=data["skillDPS"]
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] #讓亂碼正常顯示
plt.title(("降臨後衛DPS參考表"+"  BOSS :"+enemyelement+"  部位數 :"+str(traget)+"  預期時間 :"+str(time)))
plt.barh(x,y,color="blue",label="普通攻擊期望")
plt.barh(x,z,color="c",label="上位攻擊期望",left=y)
plt.barh(x,z,color="m",label="上位攻擊期望2",left=y+z)
# plt.barh(x,z2,color="yellow",label="上位攻擊期望2")
plt.yticks(x,name,fontsize=8)
for i in data.index:
    plt.text(
    int(data["normalDPS"][i]+data["skillDPS"][i]), #x軸
    i, #y軸
    round(data["skill1"][i],2), #文字
    fontsize=10,
    verticalalignment="center", #垂直對齊方式
    horizontalalignment="right") #水平

    plt.text(
    int(data["normalDPS"][i]+data["skillDPS"][i]*2), #x軸
    i, #y軸
    round(data["skill2"][i],2), #文字
    fontsize=10,
    verticalalignment="center", #垂直對齊方式
    horizontalalignment="right") #水平

plt.show()
