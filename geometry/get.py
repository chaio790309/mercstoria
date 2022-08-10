import urllib.request as req #請求
import bs4 #解析

def get(x):

    url=x
    with req.urlopen(url) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,"html.parser")

    name=root.find("h2")
    #print(name.string)

    ass=root.find_all("p",limit=24)
    n=1
    #print(ass)
    result=[]
    for a in ass:
        if n==5: #屬性
            element=""
            match a.text[len(a.span.string)+1:].replace("\n",""):
                case "炎":
                    element="fire"
                case "水":
                    element="water"
                case "風":
                    element="wind"
                case "光":
                    element="light"
                case _:
                    element="dark"
            result=result+[element]
            n+=1
        
        elif n == 6: #成長類型
            growth=0
            match a.text[len(a.span.string)+1:].replace("\n",""):
                case "早熟":
                    growth="0.12"
                case "平均":
                    growth="0.08"
                case "晩成":
                    growth="0.06"
            result=result+[growth]
            n+=1
        elif n ==8: #武器
            weapon=""
            match a.text[len(a.span.string)+1:].replace("\n",""):
                case "弓矢":
                    weapon="Bow"
                case "魔法":
                    weapon="Magic"
                case "銃弾":
                    weapon="Gun"
            result=result+[weapon]
            n+=1
        elif n in [5,6,9,10,22,23,24]: #1.國別 2.年齡 3.性別 4.星數 5.屬性 6.成長類型 7.持有武器 8.武器類型 9.體數 10.段數 11.初期HP 12.滿HP 13.滿覺HP 14.進化HP 15移速
                                    #16.手長 17.DPS 18.覺醒DPS 19.進化DPS 20.初期ATK 21.滿ATK 22.滿覺ATK 23.進化ATK 24.攻擊間隔 25.韌性 26.綜合DPS 27覺醒綜合DPS 28.進化綜合DPS
            b=a.text[len(a.span.string)+1:].replace("\n","").replace(",","").replace("体","").replace("段","")
            result=result+[b]
            n+=1
        else:
            n+=1
    if result[6]>result[5]: #pop移除特定list位置 判定是否有進化 並在文字前附加[S]
        result.pop(5)
        name="[S]"+name.string
    else:
        result.pop(6)
        name=name.string
    if result[4] == "": #單段傭兵補上1
        result[4]="1"

    element=root.find("div",class_="db_other_text") #屬性補正
    element=(element.text.replace("\n\xa0\n","")).replace("\n","").replace("炎","").replace("水","").replace("風","").replace("光","").replace("闇","").replace("％","").replace("%","")
    #print(ele)
    element=element.split("属性")
    element=element[1:]
    ele=[]
    for e in element:
        ele=ele+[round(int(e)*0.01,2)]
    # print(ele)

    return [name]+result+ele