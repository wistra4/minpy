# 04_リスト型、タプル型を使いこなす
# リストをソートする
print("<リストをソートする>")
monk_fish_team = [158, 157, 163, 157, 145]
monk_fish_team.sort()     # ソートする
print(monk_fish_team)     # リストの内容を確認

monk_fish_team.sort(reverse=True)     # ソートをする
print(monk_fish_team)     # リストの内容を確認

# ソート順をカスタマイズする
print("<ソート順をカスタマイズする>")
    tank_data = [("IV号戦車", 38, 80, 75), ("LT-38", 42, 50, 37), ("八九式中戦車", 20, 17, 57), ("III号突撃砲", 40, 50, 75), ("M3中戦車", 39, 51, 75)]

def evaluate_tankdata(tup):
    return tup[1]+tup[2]+tup[3]

evaluate_tankdata(tank_data[0])     # IV号戦車(インデックス0)
evaluate_tankdata(tank_data[4])     # M3中戦車(インデックス4)

tank_data.sort(key=evaluate_tankdata, reverse=True)
print(tank_data)

# アンパック代入
print("<アンパック代入>")
a = 1
b = 2
b, a = a, b     # 複数の要素を同時に代入する
print(a, b)

# スライスのステップ数
print("<スライスのステップ数>")
a = [1, 2, 3, 4, 5]
print(a)
print(a[1:4])     # [1:3]ではないことに注意
print(a[2:100])     # エラーにならない
print(a[::2])     # リストから偶数番目の要素を取り出す

# スライスを使った要素の代入と削除
print("<スライスを使った要素の代入と削除>")
a = [1, 2, 3, 4, 5]     # リストを作る
a[2:4] = ["Three", "Four", "Five"]     # リストの2~3番目の要素を入れ替える
print(a)     # 結果を表示

a = [1, 2, 3, 4, 5]
del a[2:]     # 3番目から最後までを削除する
print(a)