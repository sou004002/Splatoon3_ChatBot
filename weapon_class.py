import csv
WeaponList=[]
#ブキクラスの作成
class Weapon:
    name=None
    yomi=None
    genre=None
    sub=None
    spe=None
    pho=None
    position=None

    def __init__(self,N,Y,G,Su,Sp,Ph,Po):
        self.name=N
        self.yomi=Y
        self.genre=G
        self.sub=Su
        self.spe=Sp
        self.pho=Ph
        self.position=Po
file02='Weapon.csv'
with open(file02,encoding='utf8',newline='')as f:
    csvreader=csv.reader(f)
    csvheader=next(csvreader)
    for row in csvreader:
        data1=Weapon(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        WeaponList.append(data1)