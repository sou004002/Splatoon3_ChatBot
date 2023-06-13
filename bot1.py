import weapon_class
import jaconv
from janome.tokenizer import Tokenizer
import random

def search(inp):
    keylist=[]
    input_list=[]
    file01='userdic.csv'
    t=Tokenizer(file01, udic_enc="utf8")

    for token in t.tokenize(inp):
        input_list.append(token.surface)
    for j in input_list:
        for i in weapon_class.WeaponList:
            if(j==i.name):
                keylist.append(i)
        for i in weapon_class.WeaponList:
            if(j==i.genre):
                keylist.append(i)
        for i in weapon_class.WeaponList:
            if(j==i.sub):
                keylist.append(i)
        for i in weapon_class.WeaponList:
            if(j==i.spe):
                keylist.append(i)

    if(len(keylist)==0):
        for token in t.tokenize(jaconv.hira2kata(inp)):
            input_list.append(token.surface)
        for j in input_list:
            for i in weapon_class.WeaponList:
                if(j==i.name):
                    keylist.append(i)
            for i in weapon_class.WeaponList:
                if(j==i.genre):
                    keylist.append(i)
            for i in weapon_class.WeaponList:
                if(j==i.sub):
                    keylist.append(i)
            for i in weapon_class.WeaponList:
                if(j==i.spe):
                    keylist.append(i)
    return keylist

def org():
    frontlist=[]
    middlelist=[]
    backlist=[]
    ans=""
    for i in weapon_class.WeaponList:
        if(i.position=="front"):
            frontlist.append(i.name)
        elif(i.position=="middle"):
            middlelist.append(i.name)
        elif(i.position=="back"):
            backlist.append(i.name)
    ans+=random.choice(backlist)+'\n'
    ans+=random.choice(middlelist)+'\n'
    ans+=random.choice(frontlist)+'\n'
    ans+=random.choice(frontlist)
    return ans




