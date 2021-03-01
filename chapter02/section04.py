# 04_リストを使う
'''
リストはデータを順番に並べて管理する
'''

# リストを定義する
print("<リストを定義する>")
'''
リストの定義方法
[要素0, 要素1, 要素2]
'''
tokyo_temps = [15.1, 15.4, 15.2, 15.4, 17.0, 16.9]
# 東京都の平均気温のグラフ
# pip install matplotlib (terminal)
import matplotlib.pyplot as plt
plt.plot(tokyo_temps)
plt.show()

# インデックスを指定して要素を取り出す
print("<インデックスを指定して要素を取り出す>")
'''
リストの要素を取り出す記法
'''
# リスト名[要素のインデックス]
print(tokyo_temps[0])
print(tokyo_temps[5]-tokyo_temps[0])
# インデックスに-1を与えるとリストの一番最後の要素を指定できる
print(tokyo_temps[-1]-tokyo_temps[0])

# リストの連結
print("<リストの連結>")
e_tokyo_temps = [13.6, 13.5, 15.2, 14.8, 14.8]
tokyo_temps2 = e_tokyo_temps + tokyo_temps
print(tokyo_temps2)
plt.plot(tokyo_temps2)
plt.show()

# 要素の置き換え、削除
print("<要素の置き換え、削除>")
mcz = ["れに", "あかり", "かなこ", "しおり", "あやか", "ゆきな"]
print(mcz)
# 置き換え
mcz[5] = "ももか"
print(mcz)
# 削除
del mcz[0]
print(mcz)

# スライスを利用して複数の要素を取り出す
print("<スライスを利用して複数の要素を取り出す>")
'''
スライスの記法
リスト名[最初の要素のインデックス:最後の要素のインデックス+1]
'''
momotamai = mcz[1:3]
print(momotamai)
print(mcz[:2])
print(mcz[1:])

# リストのリスト - 2次元配列
print("<リストのリスト - 2次元配列>")
city_temps = [
[14.8, 14.8, 15.1, 15.4, 15.2, 15.4, 17.0, 16.9],     # 東京
[10.0, 10.4, 11.5, 11.2, 10.9, 10.6, 11.8, 12.2],     # 秋田
[16.0, 15.5, 15.9, 16.4, 15.9, 15.6, 17.5, 17.1]      # 熊本
]
# 秋田市の平均気温リストを表示する
print(city_temps[1])
# 平均気温の比較
print(city_temps[2][7]-city_temps[2][0])

plt.plot(city_temps[0])
plt.plot(city_temps[1])
plt.plot(city_temps[2])
plt.show()

# リストの合計、最大値、最小値
print("<リストの合計、最大値、最小値>")
monk_fish_team = [158, 157, 163, 157, 145]
print(sum(monk_fish_team))
print(max(monk_fish_team))
print(min(monk_fish_team))

# リストの長さを調べる
print("<リストの長さを調べる>")
print(len(monk_fish_team))
monk_sum = sum(monk_fish_team)     # 合計を計算
monk_len = len(monk_fish_team)     # 長さを調べる
monk_mean = monk_sum/monk_len      # 平均を計算
print(monk_mean) 

plt.bar([0, 1, 2, 3, 4], monk_fish_team)
plt.plot([0, len(monk_fish_team)], [monk_mean, monk_mean], color='red')
plt.show()