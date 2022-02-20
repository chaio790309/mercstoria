def atks(s): #進場攻速
    asstone=36*1.05
    realatks=s*0.6*(1-asstone*0.01)
    return realatks

def atk(a,growth): #攻擊 成長  進場攻擊
    atkstone=36*1.05
    guild=30+growth
    defaultcountrymind=15
    realatk=a*(1+(atkstone+guild+defaultcountrymind)*0.01)+a*(1+atkstone*0.01)*(1+10%-1)
    return realatk

def ele(ue,e): #屬性 補正 武器 體數
    breakseed=37.8*0.01 #1.778雙中衛破魔寵效果
    if ue in ["炎","水","風"]:
        ele=(int(e)*(1+0.12)+0.09)*(1+0.35)*(1+0.06)+breakseed*5+0.35+0.35/3+0.35*5/15
    else: #光暗副補正較高
        ele=(int(e)*(1+0.12)+0.12)*(1+0.35)*(1+0.06)+breakseed*5+0.35+0.35/3+0.35*5/15

    # if w == "銃弾": #銃技能補正
    #     skele=ele+0.3675*3-0.1*int(t)
    # else:
    #     skele=ele

    return ele #普攻補正

    #(對屬性%*(1+CM主效果%)+CM副效果%)*(1+屬性石%)*(1+屬性建築%)+破%*5+領域石%/3+補上位%*同屬數/15

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