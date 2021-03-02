# 03_タプルを使う
'''
タプルの定義方法
(要素, 要素, ...)
'''
month_names = ("January", "February", "March", "April", "May", "June", "July")
print(month_names[1])     # 2月の名前を表示する

# month_name[0] = "睦月"
'''
Traceback (most recent call last):
  File "section03.py", line 9, in <module>
    month_name[0] = "睦月"
NameError: name 'month_name' is not defined
'''

month_names = month_names + ("August", "September", "October", "November", "December")
print(month_names[11])

# タプルの利点
print("<タプルの利点>")
pref_capitals = {(43.06417, 141.34694):"北海道(札幌)",
                 (40.82444, 140.74):"青森県(青森市)",
                 (39.70361, 141.1525):"岩手県(盛岡市)"
}

loc = (39.70361, 141.1525)     # 調べたい地点の緯度、経度
for key in pref_capitals:     # キーでループ
    if loc == key:     # 調べたい地点とディクショナリのキーが同じだった
        print(pref_capitals[key])
        break     # ループを抜ける

loc = (41.768793, 140.72881)     # 調べたい地点の緯度、経度
nearest_cap = '' # 最寄りの県庁所在地名を保存する変数
nearest_dist = 10000     # 最寄りの地点までの距離を保存する変数
for key in pref_capitals:
    dist = (loc[0]-key[0])**2+(loc[1]-key[1])**2     # 緯度経度の差を二乗して距離を計算
    if nearest_dist > dist:
        nearest_dist = dist     # より近い地点が見つかったので変数を入れ替え
        nearest_cap = pref_capitals[key]
print(nearest_cap)


