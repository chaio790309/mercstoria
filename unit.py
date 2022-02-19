import urllib.request as req
url="https://xn--cckza4aydug8bd3l.gamerch.com/%E2%98%855"

with req.urlopen(url) as response:
    data=response.read().decode("utf-8")
#print(data)

import bs4
root=bs4.BeautifulSoup(data,"html.parser")
names=root.find_all("td",class_="no-min-width")
#print(units)
a=0 #記位置
s=0 #計數
ok=False #篩選
n="" #紀錄文字
b=0 #後衛數量
import geometry.get as g #寫好的函數
import urllib.parse
for name in names:
    if name.span != None: # 一個傭兵含12個<td> 其中10個class="no-min-width" 第一個不含span 0.名稱 1.武器 2.體數 3.段數 4.手長 
        if a == 0:
            n=urllib.parse.quote(name.span.string) #先取得文字
            a+=1
            s+=1
        elif a == 1:
            if name.span.string in ["弓矢","魔法","銃弾"]:
                ok=True
            a+=1
        elif a == 4:
            if (int(name.span.string) >150 and ok == True ):
                g.get("https://xn--cckza4aydug8bd3l.gamerch.com/"+n)
                b=b+1
            a+=1
        elif a < 8:
            a+=1
        else:
            a=0
            ok=False
print("總共",s,"隻5星傭兵")
print("其中有",b,"個後衛")