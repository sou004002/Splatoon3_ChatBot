import tkinter as tk
from PIL import ImageTk
import bot1

#現在の行数を把握するリスト
inputlenlist=[]
outputlenlist=[]

#メインウインドウroot 
root = tk.Tk()
root.title("ブキ判定bot")
root.geometry("600x700")
#Canvasのmessageを作成
message=tk.Canvas(root,bg="#b0e0e6")
message.create_rectangle(10,20,280,10000,fill="white",outline="white")
message.create_rectangle(290,20,570,10000,fill="#98fb98",outline="#98fb98")
message.place(x=0, y=0, width=600, height=600)
#スクロールバーの作成
bar_y = tk.Scrollbar(message, orient=tk.VERTICAL)
bar_y.pack(side=tk.RIGHT, fill=tk.Y)
bar_y.config(command=message.yview)
message.config(yscrollcommand=bar_y.set)
message.config(scrollregion=(0, 0, 300, 10000))
v = tk.StringVar() # Entryの入力を受け取る

#テキストボックスの作成
entry = tk.Entry(root, textvariable=v,font=("MSゴシック", "20"))
entry.place(x=250, y=650, width=400,height=50, anchor=tk.CENTER)
#実行ボタンの作成
button = tk.Button(root, text="実行", font=("MSゴシック", "15", "bold"),command=lambda:disp_strings(v))
button.place(x=500, y=650, anchor=tk.CENTER)

#画像の初期値を設定
photo_image = ImageTk.PhotoImage(file =".\\weapon_png\\"+bot1.weapon_class.WeaponList[0].pho)


def disp_strings(entry_v):#「実行」ボタンを押したときに作動する関数
    #残っている画像を削除
    message.delete("weapon")
    
    global photo_image
    #行数を管理するcnt
    cnt=0
    #出力用の文字列output,input
    output=""
    input=""

    #出力の文字列をリストに入れていく
    inputlist=[]
    outputlist=[]

    #これまでの行数分改行する
    for i in outputlenlist:
        output+=i*'\n'
    for i in inputlenlist:
        input+=i*'\n'    
    #テキストボックスに入力する文字列str
    str = entry_v.get()
    inputlist.append(str)
    inputlenlist.append(len(inputlist))
    #前回までの出力で改行した分、入力に改行する
    for i in outputlenlist:
        input+=i*'\n'
    #表示した分出力も改行する
    for i in inputlenlist:
        output+=i*'\n'
    #文字列inputに入力文字を足す
    for i in inputlist:
        input=input+i+"\n"
    message.create_text(550,50,text=input,anchor='ne',font=("MSゴシック", "15"))

    #テキストボックスを空にする
    entry_v.set("")

    if("編成" in str or "へんせい" in str):
        output+=bot1.org()
        outputlenlist.append(4)
        message.create_text(10,50,text=output,anchor='nw',font=("MSゴシック", "15"))
        return 0

    k=bot1.search(str)
    #outputlistに適するブキの名前を入れる
    for i in k:
        outputlist.append(i.name)
    outputlenlist.append(len(outputlist))
    #文字列outputに出力を結合
    for j in outputlist:
        output=output+j+"\n"

    if(len(outputlist)==1):
        output+="サブ："+k[0].sub+"\n"
        output+="スペシャル："+k[0].spe+"\n"
        outputlenlist.append(2)
        inputlenlist.append(2)
    if(len(outputlist)==0):
        output+="すみません。よくわかりません。\n"
        outputlenlist.append(1)

    message.create_text(10,50,text=output,anchor='nw',font=("MSゴシック", "15"))
    #出力結果が1つなら画像を表示
    if(len(outputlist)==1):
        for i in outputlenlist:
            cnt+=i
        for i in inputlenlist:
            cnt+=i
        photo_image = ImageTk.PhotoImage(file =".\\weapon_png\\"+k[0].pho)
        message.create_image(60,70+cnt*20,image=photo_image,tag="weapon")


root.mainloop()
