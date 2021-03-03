# 08_for文と組み込み型
# range()関数を使いこなす
print("<range()関数を使いこなす>")
for i in range(10, 21):
    print(i, end=" ")     # 改行せずに繰り返し変数を表示

print(range(10, 21, 2))     # 10から20まで、2つごとに増える
print(range(10, 21, 3))     # 10から19まで、3つごとに増える
print(range(20, 9, -1))     # 20から10まで、1つずつ減る

# シーケンスとループカウンタ
print("<シーケンスとループカウンタ>")
# counter = 0
for item in seq:
    # ループブロック内での処理
    counter += 1

for cnt in range(len(seq)):
    print(seq[cnt])

for cnt, item in enumerate(seq):
    print(cnt, item)

# 2つのシーケンスを作ったループ
print("<2つのシーケンスを作ったループ>")
for n, w in zip([1, 2, 3, 4], ['a', 'b', 'c', 'd']):
    print(n, w)