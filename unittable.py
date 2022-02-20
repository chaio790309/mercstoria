import geometry.allunit as au
allunit=au.allunit()
#print(allunit)

name=[]
element=[]
growth=[]
weapon=[]
traget=[]
hit=[]
atk=[]
atks=[]
fire=[]
water=[]
wind=[]
light=[]
dark=[]

a=0
for n in allunit:
    match a%13:
        case 0:
            name=name+[n]
            a+=1
        case 1:
            element=element+[n]
            a+=1
        case 2:
            growth=growth+[n]
            a+=1
        case 3:
            weapon=weapon+[n]
            a+=1
        case 4:
            traget=traget+[n]
            a+=1
        case 5:
            hit=hit+[n]
            a+=1
        case 6:
            atk=atk+[n]
            a+=1
        case 7:
            atks=atks+[n]
            a+=1
        case 8:
            fire=fire+[round(int(n)*0.01,2)]
            a+=1
        case 9:
            water=water+[round(int(n)*0.01,2)]
            a+=1
        case 10:
            wind=wind+[round(int(n)*0.01,2)]
            a+=1
        case 11:
            light=light+[round(int(n)*0.01,2)]
            a+=1
        case 12:
            dark=dark+[round(int(n)*0.01,2)]
            a+=1

# print(name)
# print(element)



import pandas as pd

unittable=pd.DataFrame({
    "name":name,
    "element":element,
    "growth":growth,
    "weapon":weapon,
    "traget":traget,
    "hit":hit,
    "atk":atk,
    "atks":atks,
    "fire":fire,
    "water":water,
    "wind":wind,
    "light":light,
    "dark":dark,
})
print(unittable)

unittable.to_csv("unit.csv",encoding="utf-8",index=False)