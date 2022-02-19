from asyncio.windows_events import NULL


def get(x):
    import urllib.request as req
    url=x
    with req.urlopen(url) as response:
        data=response.read().decode("utf-8")

    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")

    name=root.find("h2")
    #print(name.string)

    ass=root.find_all("p",limit=24)
    n=1
    #print(ass)
    re=[]
    for a in ass:
        if n in [5,6,8,9,10,16,22,23,24]: #1.國別 2.年齡 3.性別 4.星數 5.屬性 6.成長類型 7.持有武器 8.武器類型 9.體數 10.段數 11.初期HP 12.滿HP 13.滿覺HP 14.進化HP 15移速
                                    #16.手長 17.DPS 18.覺醒DPS 19.進化DPS 20.初期ATK 21.滿ATK 22.滿覺ATK 23.進化ATK 24.攻擊間隔 25.韌性 26.綜合DPS 27覺醒綜合DPS 28.進化綜合DPS
            # print(a)
            # print(a.span)
            #print(a.span.string,": ",end="")
            b=a.text[len(a.span.string)+1:].replace("\n","").replace(",","").replace("体","").replace("段","")
            re=re+[b]
            n+=1
        else:
            n+=1
    if re[7]>re[6]: #pop移除特定list位置
        re.pop(6)
    else:
        re.pop(7)
    if re[4] == "":
        re[4]="1"

    ele=root.find("div",class_="db_other_text")
    ele=(ele.text.replace("\n\xa0\n","")).replace("\n","").replace("炎","").replace("水","").replace("風","").replace("光","").replace("闇","")
    #print(ele)
    ele=ele.split("属性")
    #print(ele[1:])


    re=[name.string]+re+ele[1:]
    print(re)
