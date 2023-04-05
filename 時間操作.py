
# -*- coding: UTF-8 -*-
'''
ユーザーに入力された時が指定された時間範囲内に含まれるかどうか判断するプログラムです。
引数：　 判断されたい時間　ー＞　タイム
        開始時刻　ー＞　スタート
        終了時刻　ー＞　エンド
'''

from cgi import print_form


def 時刻＿チェック(タイム, スタート, エンド):
    if スタート < エンド:
        return (タイム >= スタート) and (タイム < エンド)
    elif スタート > エンド:
        if (タイム >= スタート) or (タイム == 0):
            return True
        else:
            return タイム < エンド
    else: #(スタート == エンド) --開始時刻と終了時刻が同じの場合は２４時間期間だと思う。
        return True

def 入力＿受け取る(メッセージ):
    ユーザー入力 = input(メッセージ)
    分けた入力 = ユーザー入力.split(" ")
    if len(分けた入力) == 3:
        try:
            ある時刻 = 数字範囲＿チェック(int(分けた入力[0]))
            if ある時刻 == -1:
                print("0から23までの数字を使って下さい。")
                return
            開始 = 数字範囲＿チェック(int(分けた入力[1]))
            if 開始 == -1:
                print("0から23までの数字を使って下さい。")
                return
            終了 = 数字範囲＿チェック(int(分けた入力[2]))
            if 終了 == -1:
                print("0から23までの数字を使って下さい。")
                return
            if 時刻＿チェック(ある時刻, 開始, 終了):
                print(str(ある時刻)+"は"+str(開始)+"から"+str(終了)+"までの範囲内に含まれる。")
            else:
                print(str(ある時刻)+"は"+str(開始)+"から"+str(終了)+"までの範囲内に含まれない。")
        except ValueError:
            print("0から23までの数字を使って下さい。")
    elif len(分けた入力) == 1:
        if 分けた入力[0] == "":
            exit()
        else:
            print("引数が足りません。")
    elif len(分けた入力) > 3:
        print("引数が多過ぎます。")
    else:
        print("引数が足りません。")
    
def 数字範囲＿チェック(value):
    if (value in range(0,24,1)):
        return value
    else:
        return -1

def main():
    print("ある時が指定された時間範囲内に含まれるかどうか判断するプログラムです。")
    print("「ある時刻　開始時刻　終了時刻」のように入力して下さい。")
    while True:
        入力＿受け取る(">")

if __name__ == "__main__":
    main()
