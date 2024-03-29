import pandas as pd #資料分析
import geometry.realability as ra #自訂進場能力
import geometry.allunit as ga #自訂全單位
import geometry.unittable as gu #自訂表格
import os #path處理路徑


print("檢查更新中...")
result=os.path.isfile("unit.csv") #確認檔案

if result:
    data=pd.read_csv("unit.csv")    
    unitcount=ga.check() #確認數量
    if unitcount != data.shape[0]:
        different=unitcount-data.shape[0]
        update=input("偵測到 "+str(different)+"筆 新資料，是否進行更新 (y/n) : ")
        while True:
            match update:
                case "y":
                    gu.unittable()
                    data=pd.read_csv("unit.csv")
                    break
                case "n":
                    print("選擇不進行資料更新")
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

while True:
    enemytarget=input("輸入敵人部位數 (2 / 3 / 4 / 5) : ")
    if enemytarget in ["2","3","4","5"]:
        target=enemytarget
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
    time=input("麻痺打法輸入預期時間 (15~36) (延時請輸入99) : ")
    if time.isdigit(): #確認為>=0數字
        if int(time)==99:
            print("敵人屬性:",enemyelement," 部位數:",target," 加成武器:",bonus2," 預期時間:","延時打法")
            break
        elif int(time)<15 or int(time)>36:
            print("無效的輸入")
        else:
            print("敵人屬性:",enemyelement," 部位數:",target," 加成武器:",bonus2," 預期時間:",time+"秒")
            break
    else:
        print("無效的輸入")
        continue





import matplotlib.pyplot as plt
filter=data["element"]==element #篩選對應屬性
data=data[filter]


#加成武器
data["bonus"]=ra.bonus(data["weapon"],bonus,data.index)

#進場攻速
data["ratks"]=ra.atks(data["atks"])

#實際體數
data["rtarget"]=ra.target(data["target"],target)

#集球速度
data["rballsec"]=ra.ballsec(data["target"],data["hit"],data["ratks"],data["rtarget"])

#一輪時間
data["round"]=ra.rround(data["target"],data["rballsec"],data["ratks"])

#進場攻擊
data["ratk"]=ra.atk(data["atk"],data["growth"])

#滿寵補正
data["relement"]=ra.element(data["element"],data[enemyelement],data.index)

#普攻期望
data["normalDPS"]=ra.normalDPS(data["rtarget"],data["ratks"],data["ratk"],data["relement"],data["bonus"])

#技能期望 判斷武器算法
data["skillDPS"]=ra.SkillDPS(data["weapon"],data["target"],data["hit"],data["relement"],data["ratk"],data.index,time,data["round"],data["bonus"])

if int(time)!=99:
    #發動1期望秒
    data["skill1"]=ra.skill1(data["round"],data["target"],data["rballsec"])

    #發動2期望秒
    data["skill2"]=ra.skill2(data["round"],data["target"],data["rballsec"])

    #發動期望次數
    data["skillnumber"]=ra.skillnumber(data["skill2"],time)

    #排序用期望傷害
    data["expectedDPS"]=ra.expectedDPS(data["normalDPS"],data["skillDPS"],data["skillnumber"])
else:
    #排序用期望傷害
    data["expectedDPS"]=ra.expectedDPS(data["normalDPS"],data["skillDPS"],1)



#排序並重置索引
    data=data.sort_values(by=["expectedDPS"],ascending=True).reset_index(drop=True)
# index=data.index.tolist() #取索引供取資料



if int(time)!=99:
    x=range(data.shape[0]) #shape回傳[列數,行數] 取得總列
    name=data["name"]
    y=data["normalDPS"] #測試值
    z=data["skillDPS"]
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] #讓亂碼正常顯示
    plt.title(("降臨後衛DPS參考表"+"  BOSS :"+enemyelement+"  部位數 :"+str(target)+"  加成 :"+bonus2+"  預期時間 :"+str(time)))
    plt.barh(x,y,color="blue",label="普通攻擊期望")
    plt.barh(x,z,color="c",label="上位攻擊期望",left=y) #left 左邊距離
    plt.barh(x,z,color="m",label="上位攻擊期望2",left=y+z)
    plt.yticks(x,name,fontsize=8)
    for i in data.index:
        plt.text(
        int(data["normalDPS"][i]+data["skillDPS"][i]), #x軸
        i, #y軸
        round(data["skill1"][i],2), #文字
        fontsize=10,
        color="w",
        verticalalignment="center", #垂直對齊方式
        horizontalalignment="right") #水平

        plt.text(
        int(data["normalDPS"][i]+data["skillDPS"][i]*2), #x軸
        i, #y軸
        round(data["skill2"][i],2), #文字
        fontsize=10,
        color="w",
        verticalalignment="center", #垂直對齊方式
        horizontalalignment="right") #水平

    plt.show()
else:
    x=range(data.shape[0]) #shape回傳[列數,行數] 取得總列
    name=data["name"]
    y=data["normalDPS"] #測試值
    z=data["skillDPS"]
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] #讓亂碼正常顯示
    plt.title(("降臨後衛DPS參考表"+"  BOSS :"+enemyelement+"  部位數 :"+str(target)+"  加成 :"+bonus2+"  預期時間 :"+"延時打法"))
    plt.barh(x,y,color="blue",label="普通攻擊期望")
    plt.barh(x,z,color="c",label="上位攻擊期望",left=y) #left 左邊距離
    plt.yticks(x,name,fontsize=8)
    for i in data.index:
        plt.text(
        int(data["normalDPS"][i]+data["skillDPS"][i]), #x軸
        i, #y軸
        round((data["normalDPS"][i]+data["skillDPS"][i])/1000000,2), #文字
        fontsize=10,
        color="w",
        verticalalignment="center", #垂直對齊方式
        horizontalalignment="right") #水平

    plt.show()