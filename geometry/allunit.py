import urllib.request as req


import geometry.get as g #寫好的函數
import urllib.parse #將文字轉碼給url用
import bs4

def allunit():
    url="https://xn--cckza4aydug8bd3l.gamerch.com/%E2%98%855"

    with req.urlopen(url) as response: #開啟網頁並獲得data
        data=response.read().decode("utf-8")
    #print(data)


    root=bs4.BeautifulSoup(data,"html.parser") #解析網頁data
    names=root.find_all("td",class_="no-min-width")
    #print(units)
    a=0 #記位置
    s=0 #計數
    ok=False #篩選
    n="" #紀錄文字
    b=0 #後衛數量
    allunit=[]
    for name in names:
        if name.span != None: # 一個傭兵含12個<td> 其中10個class="no-min-width" 第一個不含span 0.名稱 1.武器 2.體數 3.段數 4.手長 
            match a%9:
                case 0:
                    n=urllib.parse.quote(name.span.string) #取得文字
                    a+=1
                    s+=1
                case 1:
                    if name.span.string in ["弓矢","魔法","銃弾"]: #確認條件
                        ok=True
                    a+=1
                case 4:
                    if (int(name.span.string) >150 and ok == True ): #確認條件2
                        result=g.get("https://xn--cckza4aydug8bd3l.gamerch.com/"+n)
                        print(result)
                        b=b+1
                        allunit=allunit+result
                    a+=1
                    ok=False

                case _:
                    a+=1
    # print(allunit)
    print("總共",s,"個5星傭兵")
    print("其中有",b,"個符合條件")

    return allunit

def check():
    url="https://xn--cckza4aydug8bd3l.gamerch.com/%E2%98%855"
    with req.urlopen(url) as response: #開啟網頁並獲得data
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,"html.parser") #解析網頁data
    names=root.find_all("td",class_="no-min-width")
    a=0 #記位置
    b=0 #計數
    ok=False #篩選
    for name in names:
        if name.span != None:
            match a%9:
                case 1:
                    if name.span.string in ["弓矢","魔法","銃弾"]: #確認條件
                        ok=True
                    a+=1
                case 4:
                    if (int(name.span.string) >150 and ok == True ): #確認條件2
                        b=b+1
                    a+=1
                    ok=False
                case _:
                    a+=1
    return b #回傳後衛數量