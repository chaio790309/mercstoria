def bonus(weapon:str,bonus:str,index:list)->list:
    result=[]
    for i in index:
        if weapon[i] == bonus:
            if weapon[i] == "Bow":
                result+=[1.35*1.175]
            else:
                result+=[1.35]
        else:
            if weapon[i] == "Bow":
                result+=[1.175]
            else:
                result+=[1]
    return result

def atks(atks:float)->list: #進場攻速
    asstone=36*1.05
    realatks=round(atks*0.6*(1-asstone*0.01),3)
    return realatks

def target(unittraget:list,enemytraget:int)->list:
    result=[]
    for t in unittraget:
        result+=[min(t,int(enemytraget))]
    return result

def ballsec(target:int,hit:int,ratks:float,realtraget)->list:
    realballsec=(0.15/(target*hit)+ratks/15)*realtraget*hit/ratks
    return realballsec

def rround(target:int,ballsec:float,ratks:float)->list:
    realround=3.625+target+5/ballsec+ratks
    return realround

def atk(atk:float,growth:float)->list: #攻擊 成長  進場攻擊
    atkstone=(36+7*1.05)*0.01
    guild=30*0.01+growth
    defaultcountrymind=15
    realatk=round((atk*(1+(atkstone+guild+defaultcountrymind))+atk*(1+atkstone)*(1+10%-1))/5,2)
    return realatk

def element(unitelement:str,element:float,index:list)->list: #屬性 補正 武器 體數 
    breakseed=38.7*0.01 #1.798雙中衛破魔寵效果
    result=[]
    for i in index: #用在其他地方可能會有問題
        if unitelement[i] in ["fire","water","wind"]:
            result+=[(element[i]*(1+0.12)+0.09)*(1+0.35)*(1+0.06)+breakseed*5+0.35/3+0.35*5/15]
        else:
            result+=[(element[i]*(1+0.12)+0.12)*(1+0.35)*(1+0.06)+breakseed*5+0.35/3+0.35*5/15]
    return result #普攻補正

def normalDPS(target:int,atks:float,atk:float,ele:float,bonus:float)->list:
    soulseed=39*0.01 #1.79雙中衛魂魔寵效果
    nDPS=round(atk*3.9*target/atks*ele*bonus*(1+soulseed)**5,2)
    return nDPS
    #基本攻擊力*Guts攻擊*(1+陣型%)*(1+魂%)^5*屬性補正%*外皮%*武器特攻%/5

def SkillDPS(weapon:str,target:int,hit:int,element:float,atk:float,index:list,time:int,bonus:float)->list:
    soulseed=39*0.01 #1.779雙中衛魂魔寵效果
    result=[]
    for i in index:
        if weapon[i] == "Bow":
            match target[i]:
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
            result+=[(36.75/5+5.5-(1/2+(target[i]+hit[i])/2))*e*(atk[i]*3.9)*element[i]*bonus[i]*(1+soulseed)**5/int(time)]
        elif weapon[i] == "Magic":
            result+=[(36.75/5+11-(target[i]/2+hit[i]*0.3))*(atk[i]*3.9)*element[i]*bonus[i]*(1+soulseed)**5/int(time)]
        else:
            result+=[(36.75/5+13.5-(target[i]+hit[i])/2)*(atk[i]*3.9)*(element[i]+(36.75*3-target[i]*10)*0.01)*bonus[i]*(1+soulseed)**5/int(time)]
    return result

def skill1(round:float,target:int,rballsec:float)->list:
    skill1=round-(3.625+target)-2/rballsec
    return skill1


def skill2(round:float,target:int,rballsec:float)->list:
    skill2=round*2-(3.625+target)-2/rballsec
    return skill2

def skillnumber(skill2:list,time:int)->list:
    result=[]
    for s in skill2:
        if s>int(time)+3:
            result+=[1]
        else:
            result+=[2]
    return result

def expectedDPS(normaldps:float,skilldps:float,skillnumber:int)->list:
    result=normaldps+skilldps*skillnumber
    return result