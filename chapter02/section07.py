# 07_関数を使う
# 関数とは
print("<関数とは>")
the_list = [101, 123, 152, 123]
summary = 0     # 合計するための変数を作成しておく
for item in the_list:     # リストでループを組む
    summary = summary+item     # リストの要素を合計

print(summary)

# 関数を呼び出す
print("<関数を呼び出す>")
'''
関数名(引数1, 引数2 ...)
'''
print(abs(10))
print(-200)

# 関数の引数
print("<関数の引数>") 
print(int ("100"))     # 文字列を10進数の数値に変換
print(int("100", 2))     # 文字列を2進数の数値に見立てて変換
print(int("100", 16))     # 文字列を16進数の数値に見立てて変換

# 関数を定義する
print("関数を定義する")
'''
関数を定義する記法
def 関数名():
    関数ブロック
'''
def destiny_tank():
    tanks = ["IV号戦車D型", "III号戦車J型", "チャーチル Mk.VII", "M4シャーマン", "P40重戦車", "T-34/76"]     # 戦車のリスト
    num = input("好きな数字を入力してください:")     # 数字を入力する
    idx = int(num) % len(tanks)     # 入力値をリストのインデックスに変換
    print("あなたの運命の戦車は")
    print(tanks[idx])     # 結果を表示する
destiny_tank()
# 引数を定義する
print("<引数を定義する>")
'''
def 関数名(引数1, 引数2 ...):
    関数ブロック
'''
def destiny_tank2(num):
    tanks = ["IV号戦車D型", "III号戦車J型", "チャーチル Mk.VII", "M4シャーマン", "P40重戦車", "T-34/76"]     # 戦車のリスト
    idx = num % len(tanks)
    print("あなたの運命の戦車は")
    print(tanks[idx])

num_str = input("好きな数字を入力してください")
num = int(num_str)
destiny_tank2(num)

from random import randint
num  = randint(0, 10)     # 乱数を生成
destiny_tank2(num)     # 生成した乱数を関数に渡す

# 関数の戻り値
print("<関数の戻り値>")
def destiny_tank3(num):
    tanks = ["IV号戦車D型", "III号戦車J型", "チャーチル Mk.VII", "M4シャーマン", "P40重戦車", "T-34/76"]     # 戦車のリスト
    idx = num % len(tanks)     # 入力値をリストのインデックスに変換
    return tanks[idx]     # 結果を戻り値として返す

from random import randint
num = randint(0, 10)
tank = destiny_tank3(num)
print("今日あなたが乗るべき幸運の戦車は", tank, "です")

# ローカル変数
print("<ローカル変数>")
# ローカル変数を関数の外で使う
def test_func(arg1):
    inner_var = 100
    print(arg1+inner_var)

test_func(10)     # 関数を呼び出す
# print(inner_var)     # 関数内で定義した変数を表示
'''
Traceback (most recent call last):
  File "07.py", line 77, in <module>
    print(inner_var)
NameError: name 'inner_var' is not defined
'''
# ローカル変数を関数の外で使う
monk_fish_team = [158, 157, 163, 157, 145]

total = sum(monk_fish_team)
length = len(monk_fish_team) 
mean = total/length
variance = 0

for height in monk_fish_team:
    variance += (height-mean)**2     # 身長から平均を引いて二乗を足す

variance = variance/length     # 足した数値を要素数で割って分散を求める
print(variance)

volleyball_team = [143, 167, 170, 165]

total2 = sum(volleyball_team)     # リストの合計
length2 = len(volleyball_team)     # リストの要素数(長さ)
mean2 = total2/length2     # 平均を求める
variance2 = 0     # 分散を計算するための変数

for height in volleyball_team:
    variance2 += (height-mean2)**2     # 身長から平均を引いて二乗を足す

variance2 = variance2/length2     # 足した数値を要素数で割って分散を求める
print(variance2)

# calc_variance()関数の定義
def calc_variance(a_list):     # 分散を求める関数
    total = sum(a_list)      # リストの合計
    length = len(a_list)     # リストの要素数(長さ)
    mean = total/length     # 平均を求める
    variance = 0     # 分散を計算するための変数

    for height in a_list:
        variance += (height-mean)**2     # 身長から平均を引いて二乗を足す
    variance = variance/len(a_list)     # 足した数値を要素数で割って分散を求める

    return variance     # 求めた分散を戻り値として返す

monk_fish_team = [158, 157, 163, 157, 145]
volleyball_team = [143, 167, 170, 165]
pravda_team = [127, 172, 140, 160, 174]

monk_team_variance = calc_variance(monk_fish_team)
volley_team_variance = calc_variance(volleyball_team)
pravda_team_variance = calc_variance(pravda_team)

print(monk_team_variance**0.5)
print(volley_team_variance**0.5)
print(pravda_team_variance**0.5)