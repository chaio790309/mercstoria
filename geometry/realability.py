
def atks(s): #進場攻速
    asstone=36*1.05
    realatks=round(s*0.6*(1-asstone*0.01),3)
    return realatks

def traget(u,e,index):
    # for t in index:
    #     u[t]=min(int(u[t]),int(e))
    # return u
    for t in index:
        if int(u[t])>int(e):
            u[t]=int(e)
    return u

def ballsec(t,h,ratks,rt):
    realballsec=(0.15/(t+h)+ratks/15)*rt*h/ratks
    return realballsec

def rround(t,rb,ratks):
    realround=3.625+t+5/rb+ratks
    return realround

def atk(a,growth): #攻擊 成長  進場攻擊
    atkstone=(36+7)*1.05*0.01
    guild=30*0.01+growth
    defaultcountrymind=15
    realatk=round(a*(1+(atkstone+guild+defaultcountrymind))+a*(1+atkstone)*(1+10%-1),2)
    return realatk

def elefww(ue,e,index): #屬性 補正 武器 體數 
    breakseed=37.8*0.01 #1.778雙中衛破魔寵效果
    for u in index: #用在其他地方可能會有問題
        if ue[u] in ["fire","water","wind"]:
            ele=(e*(1+0.12)+0.09)*(1+0.35)*(1+0.06)+breakseed*5+0.35+0.35/3+0.35*5/15
        else:
            ele=(e*(1+0.12)+0.12)*(1+0.35)*(1+0.06)+breakseed*5+0.35+0.35/3+0.35*5/15
    return ele #普攻補正

def normalDPS(t,atks,atk,ele,b):
    soulseed=38.7*0.01 #1.779雙中衛魂魔寵效果
    nDPS=round(atk*3.9*t/atks*ele*b*(1+soulseed)**5/5,2)
    return nDPS
    #基本攻擊力*Guts攻擊*(1+回復陣型%)*(1+魂%)^5*屬性補正%*外皮%*武器特攻%/5

def SkillDPS(weapon,traget,hit,element,atk,index,time):
    for w in index:
        if weapon[w] == "Bow":
            weapon[w]=11
        elif weapon[w] == "Magic":
            weapon[w]=22
        else:
            weapon[w]=33
    return weapon
    
def htep(t): #弓上位期望段數
    e=0
    match t:
        case 1:
            e=1.9
        case 2:
            e=2.7
        case 3:
            e=3.33
        case 4:
            e=3.83
        case 5:
            e=4.26
    return e