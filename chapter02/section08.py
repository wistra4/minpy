# 08_モジュールを使う
# モジュールをインポート(import)する
print("<モジュールをインポート(import)する>")
'''
import文でモジュールを読み込むための記法
import モジュール名
'''
import random     # randomモジュールを読み込む

print(random.random())     # 0<x<1の乱数を得る
print(random.randint(0, 6))     # 0<=x<=6の乱数を得る
a_list = [0, 1, 2, 3, 4, 5]
random.shuffle(a_list)     # リストをランダムに入れ替える
print(a_list)
print(random.choice(a_list))     # リストの要素を1つランダムに選ぶ

# import文のas
'''
asを使ったimport文の記法
import モジュール名 as 読み込む名前
'''

# fromを使ったインポート
print("<fromを使ったインポート>")
from statistics import median

monk_fish_team = [158, 157, 163, 157, 145]
volleyball_team = [143, 167, 170, 165]
print(median(monk_fish_team))
print(median(volleyball_team))

# モジュールの探し方
print("<モジュールの探し方>")
print("http://docs.python.jp/3/ ")