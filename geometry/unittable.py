import geometry.allunit as au
import pandas as pd

def unittable():
    allunit=au.allunit()
    #print(allunit)

    unittable=pd.DataFrame({
        "name":allunit[0::13],
        "element":allunit[1::13],
        "growth":allunit[2::13],
        "weapon":allunit[3::13],
        "target":allunit[4::13],
        "hit":allunit[5::13],
        "atk":allunit[6::13],
        "atks":allunit[7::13],
        "fire":allunit[8::13],
        "water":allunit[9::13],
        "wind":allunit[10::13],
        "light":allunit[11::13],
        "dark":allunit[12::13],
    })
    print(unittable)

    unittable.to_csv("unit.csv",encoding="utf-8",index=False) #避免左邊多一排