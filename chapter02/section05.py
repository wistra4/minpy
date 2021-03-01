# 05_for分でループを使う
'''
for分の記法
for 繰り返し変数 in シーケンス:
    ループ内で実行するブロック
'''
mcz = ['れに', 'かなこ', 'しおり', 'あやか', 'ももか']
for member in mcz:
    print(member)
print(mcz)
# 分散を計算する
monk_fish_team = [158, 157, 163, 157, 145]

total = sum(monk_fish_team)     # リストの合計
length = len(monk_fish_team)     # リストの要素数(長さ)
mean = total/length     # 平均を求める
variance = 0     # 分散を計算するための変数

for height in monk_fish_team:
    variance += (height-mean)**2     # 身長から平均を引いて二乗して数を足す

variance = variance/length     # 足した数値を要素数で割って分散を求める
print(variance)
# 標準偏差の計算
print(variance**0.5)

# 別のリストの標準偏差を計算する
volleyball_team = [143, 167, 170, 165]

total2 = sum(volleyball_team)
length2 = len(volleyball_team)
mean2 = total2/length2
variance2 = 0

for height in volleyball_team:
    variance2 += (height-mean2)**2

variance2 = variance2/length2
print(variance2)
print(variance2**0.5)

# range()関数
print("<range()関数>")
for cnt in range(10):
    print(cnt)
# 複利計算の例
savings = 100     # 元金
for i in range(15):     # 15年分繰り返すループ
    savings += savings*0.05
print(savings)